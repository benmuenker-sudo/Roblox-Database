"""Synthetisiert alle Referenz-Sounds der Roblox-Datenbank (nur numpy).

Aufruf (aus dem Repo-Hauptordner):
    python3 tools/audio/erzeuge_audio.py          # alle Sounds -> assets/audio/*.wav + *.ogg
    python3 tools/audio/erzeuge_audio.py name ... # nur bestimmte Sounds (ohne Endung)

Alle Klaenge sind selbst erzeugt (additive Synthese, FM, gefiltertes Rauschen),
also frei von fremden Rechten. WAV: 44,1 kHz, 16 Bit, mono. OGG: Vorbis via ffmpeg.
Loops werden per Kreis-Faltung (FFT) bzw. "Tail-Folding" nahtlos gemacht.
"""
import os
import subprocess
import sys
import wave

import numpy as np

SR = 44100
PEAK = 10 ** (-1 / 20)  # -1 dBFS
ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "assets", "audio")
RNG = np.random.default_rng(20261024)


# ----------------------------------------------------------------------------
# Grundbausteine
# ----------------------------------------------------------------------------
def T(dur):
    return np.arange(int(round(dur * SR))) / SR


def hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)


def silence(dur):
    return np.zeros(int(round(dur * SR)))


def place(buf, x, start):
    """x an Position start (Sekunden) in buf addieren (buf wird ggf. verlaengert)."""
    i = int(round(start * SR))
    end = i + len(x)
    if end > len(buf):
        buf = np.concatenate([buf, np.zeros(end - len(buf))])
    buf[i:end] += x
    return buf


def env_exp(n_or_t, decay, attack=0.002):
    t = n_or_t if isinstance(n_or_t, np.ndarray) else T(n_or_t)
    a = np.clip(t / max(attack, 1e-6), 0, 1)
    return a * np.exp(-t / decay)


def env_adsr(dur, a, d, s, r):
    t = T(dur)
    e = np.ones_like(t) * s
    e[t < a] = t[t < a] / a
    m = (t >= a) & (t < a + d)
    e[m] = 1 - (1 - s) * (t[m] - a) / d
    rel = t > dur - r
    e[rel] *= np.clip((dur - t[rel]) / r, 0, 1)
    return e


def sine(f, t, phase=0.0):
    return np.sin(2 * np.pi * f * t + phase)


def sweep(f0, f1, t, curve="exp"):
    """Sinus mit Frequenzverlauf f0 -> f1 ueber die Laenge von t."""
    dur = t[-1] if len(t) > 1 else 1
    if curve == "exp":
        f = f0 * (f1 / f0) ** (t / dur)
    else:
        f = f0 + (f1 - f0) * t / dur
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph), f


def additive(f, t, amps, decays=None, detune=None):
    out = np.zeros_like(t)
    for k, a in enumerate(amps, start=1):
        fk = f * k * (1 + (detune[k - 1] if detune else 0))
        if fk > SR * 0.45:
            break
        p = a * np.sin(2 * np.pi * fk * t + RNG.uniform(0, 2 * np.pi))
        if decays:
            p *= np.exp(-t / decays[k - 1])
        out += p
    return out


def bell(f, dur, decay=0.6, bright=1.0):
    t = T(dur)
    ratios = [1, 2.0, 2.76, 4.07, 5.4, 6.8]
    amps = [1, 0.55, 0.35, 0.2 * bright, 0.12 * bright, 0.06 * bright]
    out = np.zeros_like(t)
    for r, a in zip(ratios, amps):
        if f * r < SR * 0.45:
            out += a * np.sin(2 * np.pi * f * r * t) * np.exp(-t / (decay / (0.6 + r * 0.4)))
    return out * np.clip(t / 0.002, 0, 1)


def fm(fc, t, ratio, index_env, amp_env):
    mod = index_env * np.sin(2 * np.pi * fc * ratio * t)
    return amp_env * np.sin(2 * np.pi * fc * t + mod)


def epiano(f, dur, vel=1.0):
    t = T(dur)
    idx = 1.8 * vel * np.exp(-t / 0.35) + 0.25
    amp = env_exp(t, 1.4, 0.004)
    tone = fm(f, t, 1.0, idx, amp)
    tine = 0.15 * vel * np.sin(2 * np.pi * f * 14 * t) * np.exp(-t / 0.03)
    return (tone + tine) * vel


def brass(f, dur, a=0.04, r=0.12, vib=True):
    t = T(dur)
    bright = 2.0 + 7.0 * np.clip(t / (a * 2.5), 0, 1) - 2.0 * np.clip((t - a * 3) / 0.6, 0, 1)
    fv = f * (1 + (0.006 * np.sin(2 * np.pi * 5.5 * t) * np.clip((t - 0.15) / 0.3, 0, 1) if vib else 0))
    ph = 2 * np.pi * np.cumsum(fv) / SR
    out = np.zeros_like(t)
    for k in range(1, 26):
        if f * k > 11000:
            break
        out += (1.0 / k) * np.exp(-k / bright) * np.sin(k * ph)
    return out * env_adsr(dur, a, 0.15, 0.8, r)


def saw_pad(f, dur, voices=3, cents=9, a=0.4, r=0.8, cutoff_h=10):
    t = T(dur)
    out = np.zeros_like(t)
    for v in range(voices):
        det = 2 ** ((v - (voices - 1) / 2) * cents / 1200)
        ph0 = RNG.uniform(0, 2 * np.pi)
        for k in range(1, cutoff_h + 1):
            if f * det * k > 9000:
                break
            out += (1.0 / k) * np.exp(-k / (cutoff_h * 0.5)) * np.sin(2 * np.pi * f * det * k * t + ph0 * k)
    return out / voices * env_adsr(dur, a, 0.3, 0.85, r)


def noise(dur):
    return RNG.standard_normal(int(round(dur * SR)))


# ---- FFT-Filter (zero-phase). circular=True -> fuer nahtlose Loops ----
def fft_filter(x, lo=None, hi=None, order=2, circular=False, tilt=None):
    n = len(x)
    pad = 0 if circular else min(SR, n)
    X = np.fft.rfft(np.concatenate([x, np.zeros(pad)]))
    f = np.fft.rfftfreq(n + pad, 1 / SR)
    H = np.ones_like(f)
    if hi is not None:  # Tiefpass
        H *= 1 / np.sqrt(1 + (f / hi) ** (2 * order))
    if lo is not None:  # Hochpass
        with np.errstate(divide="ignore"):
            H *= 1 / np.sqrt(1 + (lo / np.maximum(f, 1e-3)) ** (2 * order))
    if tilt is not None:  # z. B. -3 dB/Oktave = rosa Rauschen (tilt=-0.5)
        H *= np.maximum(f, 20) ** tilt
    y = np.fft.irfft(X * H, n + pad)
    return y[:n] if circular else y[:n]


def svf(x, fc, q=0.7, mode="bp"):
    """Zeitvariabler State-Variable-Filter (fc als Array oder Zahl)."""
    fc = np.broadcast_to(np.asarray(fc, dtype=float), x.shape)
    low = band = 0.0
    out = np.empty_like(x)
    damp = 1.0 / q
    for i in range(len(x)):
        f = 2 * np.sin(np.pi * min(fc[i], SR * 0.2) / SR)
        high = x[i] - low - damp * band
        band += f * high
        low += f * band
        out[i] = band if mode == "bp" else (low if mode == "lp" else high)
    return out


def reverb_ir(dur=1.6, decay=0.5, lo=200, hi=7000):
    t = T(max(dur, decay * 7.0))
    ir = RNG.standard_normal(len(t)) * np.exp(-t / decay)
    ir = fft_filter(ir, lo=lo, hi=hi)
    ir[0] += 0.0
    return ir / np.sqrt(np.sum(ir ** 2))


def reverb(x, mix=0.25, dur=1.6, decay=0.5, circular=False):
    ir = reverb_ir(dur, decay)
    if circular:
        n = len(x)
        irp = np.zeros(n)
        irp[:min(n, len(ir))] = ir[:n]
        wet = np.fft.irfft(np.fft.rfft(x) * np.fft.rfft(irp), n)
        return x + mix * wet
    n = len(x) + len(ir)
    wet = np.fft.irfft(np.fft.rfft(x, n) * np.fft.rfft(ir, n), n)
    out = np.concatenate([x, np.zeros(len(ir))]) + mix * wet
    return out


def fold(buf, length):
    """Alles hinter `length` auf den Anfang addieren -> nahtloser Loop."""
    n = int(round(length * SR))
    out = buf[:n].copy()
    rest = buf[n:]
    while len(rest):
        k = min(n, len(rest))
        out[:k] += rest[:k]
        rest = rest[k:]
    return out


def fades(x, fin=0.003, fout=0.02):
    x = x.copy()
    a, b = int(fin * SR), int(fout * SR)
    if a:
        x[:a] *= np.linspace(0, 1, a)
    if b:
        x[-b:] *= np.linspace(1, 0, b) ** 2
    return x


def trim(x, thresh=1e-3):
    idx = np.nonzero(np.abs(x) > thresh * np.max(np.abs(x)))[0]
    return x[: idx[-1] + 1] if len(idx) else x


def norm(x):
    m = np.max(np.abs(x))
    return x * (PEAK / m) if m > 0 else x


# ----------------------------------------------------------------------------
# Sounds
# ----------------------------------------------------------------------------
def muenze(pitch=1.0):
    n1, n2 = hz(84) * pitch, hz(91) * pitch  # C6 -> G6
    buf = silence(0.5)
    t1 = T(0.075)
    a = (np.sign(np.sin(2 * np.pi * n1 * t1)) * 0.25 + np.sin(2 * np.pi * n1 * t1)) * env_exp(t1, 0.05)
    buf = place(buf, a * 0.6, 0)
    t2 = T(0.42)
    b = (np.sin(2 * np.pi * n2 * t2) + 0.3 * np.sin(2 * np.pi * n2 * 2 * t2) * np.exp(-t2 / 0.05)) * env_exp(t2, 0.13)
    b += 0.35 * fm(n2 * 2, t2, 3.5, 2.0 * np.exp(-t2 / 0.04), np.exp(-t2 / 0.07))
    buf = place(buf, b, 0.065)
    buf = fft_filter(buf, lo=300)
    return fades(trim(buf), 0.001, 0.03)


def pling_leiter():
    notes = [84, 86, 88, 91, 93]  # C6 D6 E6 G6 A6 (Pentatonik)
    buf = silence(1.3)
    for i, m in enumerate(notes):
        g = 0.65 + 0.09 * i
        buf = place(buf, g * bell(hz(m), 0.6, decay=0.35 + 0.05 * i, bright=0.8), i * 0.09)
    sp = sum(0.12 * bell(hz(100 + k), 0.4, 0.15) for k in (0, 4, 7))
    buf = place(buf, sp, 0.45)
    buf = reverb(buf, 0.18, 1.0, 0.25)
    return fades(trim(buf), 0.001, 0.05)


def pop_klein():
    t = T(0.14)
    s, _ = sweep(620, 170, t)
    x = s * env_exp(t, 0.035, 0.001)
    x += 0.15 * fft_filter(noise(0.14), hi=2500) * np.exp(-t / 0.006)
    return fades(x, 0.0005, 0.02)


def ui_klick():
    t = T(0.05)
    x = 0.6 * np.sin(2 * np.pi * 1900 * t) * np.exp(-t / 0.006)
    x += 0.5 * fft_filter(noise(0.05), lo=1500, hi=9000) * np.exp(-t / 0.003)
    x += 0.4 * np.sin(2 * np.pi * 420 * t) * np.exp(-t / 0.01)
    return fades(x, 0.0003, 0.01)


def ui_oeffnen(down=False):
    t = T(0.24)
    f0, f1 = (950, 420) if down else (420, 950)
    s, _ = sweep(f0, f1, t)
    x = s * env_adsr(0.24, 0.01, 0.08, 0.6, 0.12)
    x += 0.5 * np.sin(2 * np.pi * (hz(79) if not down else hz(72)) * t) * env_exp(t, 0.06) * (t > 0.1)
    nz = fft_filter(noise(0.24), lo=800, hi=5000) * env_adsr(0.24, 0.08, 0.05, 0.3, 0.12) * 0.12
    x += nz
    return fades(x, 0.002, 0.03)


def ui_fehler():
    buf = silence(0.42)
    for i, f in enumerate([233.08, 196.0]):
        t = T(0.16)
        sq = np.sign(np.sin(2 * np.pi * f * t)) * 0.5 + np.sin(2 * np.pi * f * t)
        x = fft_filter(sq, hi=1800) * env_adsr(0.16, 0.004, 0.04, 0.7, 0.05)
        buf = place(buf, x, i * 0.17)
    return fades(trim(buf), 0.002, 0.03)


def kauf_erfolg():
    buf = muenze(1.0) * 0.6
    chord = [72, 76, 79, 84]
    for i, m in enumerate(chord):
        buf = place(buf, 0.45 * bell(hz(m), 0.9, 0.45, 0.9) + 0.25 * epiano(hz(m), 0.9), 0.12 + i * 0.06)
    for k in range(6):
        buf = place(buf, 0.08 * bell(hz(96 + RNG.integers(0, 12)), 0.3, 0.1), 0.35 + k * 0.05)
    buf = reverb(buf, 0.2, 1.2, 0.3)
    return fades(trim(buf), 0.001, 0.08)


def level_up():
    buf = silence(2.2)
    seq = [(67, 0.0, 0.12), (72, 0.12, 0.12), (76, 0.24, 0.12), (79, 0.36, 0.3)]
    for m, st, d in seq:
        buf = place(buf, 0.5 * brass(hz(m), d + 0.1, a=0.02, r=0.08, vib=False), st)
    for m in (72, 76, 79, 84):
        buf = place(buf, 0.32 * brass(hz(m), 1.5, a=0.03, r=0.6), 0.62)
    t = T(0.5)
    kick, _ = sweep(110, 45, t)
    buf = place(buf, 0.9 * kick * env_exp(t, 0.12), 0.62)
    cym = fft_filter(noise(1.5), lo=5000) * env_exp(T(1.5), 0.4) * 0.25
    buf = place(buf, cym, 0.62)
    for k in range(8):
        buf = place(buf, 0.07 * bell(hz(96 + [0, 4, 7, 12][k % 4]), 0.4, 0.15), 0.7 + k * 0.07)
    buf = reverb(buf, 0.22, 1.6, 0.45)
    return fades(trim(buf), 0.002, 0.15)


def mythic_drop():
    # 1) Aufbau: Riser (Rauschen + steigender Ton), 1,3 s
    rd = 1.3
    t = T(rd)
    fc = 300 * (12000 / 300) ** (t / rd)
    riser = svf(noise(rd) * 0.6, fc, q=2.0) * (t / rd) ** 2
    tone, _ = sweep(hz(48), hz(72), t)
    riser += 0.25 * tone * (t / rd) ** 1.5
    buf = riser
    # 2) Stille vor dem Impact: 0,28 s
    imp = rd + 0.28
    # 3) Impact: Boom + Crack
    ti = T(1.2)
    boom, _ = sweep(90, 32, ti)
    buf = place(buf, 1.0 * boom * env_exp(ti, 0.35, 0.001), imp)
    buf = place(buf, 0.5 * fft_filter(noise(0.4), lo=600, hi=9000) * env_exp(T(0.4), 0.06, 0.0005), imp)
    # 4) Grosser Akkord (C-Dur add9, Pad + Brass)
    for m in (48, 60, 64, 67, 74, 79):
        buf = place(buf, 0.18 * saw_pad(hz(m), 2.6, a=0.02, r=1.6, cutoff_h=14), imp)
        if m >= 60:
            buf = place(buf, 0.12 * brass(hz(m), 1.4, a=0.02, r=0.8), imp)
    # 5) Funkeln
    for k in range(18):
        m = 96 + [0, 2, 4, 7, 9, 12, 14, 16][k % 8]
        buf = place(buf, 0.06 * bell(hz(m), 0.5, 0.18), imp + 0.05 + k * 0.08 + RNG.uniform(0, 0.03))
    buf = reverb(buf, 0.3, 2.4, 0.7)
    return fades(trim(buf), 0.01, 0.3)


def whoosh_impact():
    wd = 0.38
    t = T(wd)
    fc = 400 + 3200 * np.sin(np.pi * t / wd) ** 2
    wh = svf(noise(wd), fc, q=1.4) * np.sin(np.pi * t / wd) ** 1.5 * 0.9
    buf = wh
    ti = T(0.6)
    thump, _ = sweep(140, 45, ti)
    buf = place(buf, 1.0 * thump * env_exp(ti, 0.12, 0.0008), wd - 0.02)
    crack = fft_filter(noise(0.25), lo=900, hi=8000) * env_exp(T(0.25), 0.03, 0.0005)
    buf = place(buf, 0.6 * crack, wd - 0.02)
    buf = reverb(buf, 0.15, 1.0, 0.3)
    return fades(trim(buf), 0.005, 0.06)


def treffer_schwer():
    t = T(0.6)
    th, _ = sweep(95, 38, t)
    x = 1.0 * th * env_exp(t, 0.16, 0.0008)
    nz = fft_filter(noise(0.6), lo=200, hi=5000) * env_exp(t, 0.04, 0.0005)
    x += 0.7 * np.tanh(3 * nz)
    x += 0.15 * bell(310, 0.6, 0.12)
    x = np.tanh(1.6 * x) / np.tanh(1.6)
    x = reverb(x, 0.12, 0.8, 0.2)
    return fades(trim(x), 0.0005, 0.05)


def ernte_weich():
    buf = pop_klein() * 0.5
    t = T(0.25)
    rustle = fft_filter(noise(0.25), lo=1500, hi=6000) * env_adsr(0.25, 0.02, 0.05, 0.4, 0.15) * 0.25
    buf = place(buf, rustle, 0.0)
    tm = T(0.45)
    mar = (np.sin(2 * np.pi * hz(79) * tm) + 0.25 * np.sin(2 * np.pi * hz(79) * 4 * tm) * np.exp(-tm / 0.02)) * env_exp(tm, 0.12)
    buf = place(buf, 0.6 * mar, 0.04)
    buf = fft_filter(buf, hi=7000)
    return fades(trim(buf), 0.001, 0.04)


def wachstum_sparkle():
    buf = silence(1.6)
    n = 22
    for k in range(n):
        st = 1.0 * (k / n) ** 0.8
        m = 88 + RNG.integers(0, 22)
        buf = place(buf, (0.05 + 0.04 * k / n) * bell(hz(m), 0.4, 0.12, 1.2), st)
    shimmer = fft_filter(noise(1.4), lo=6000) * env_adsr(1.4, 0.6, 0.2, 0.5, 0.6) * 0.04
    buf = place(buf, shimmer, 0)
    sw_, _ = sweep(hz(72), hz(96), T(1.0))
    buf = place(buf, 0.08 * sw_ * env_adsr(1.0, 0.5, 0.1, 0.6, 0.4), 0)
    buf = reverb(buf, 0.3, 1.4, 0.4)
    return fades(trim(buf), 0.01, 0.1)


def nacht_warnung():
    buf = silence(3.6)
    t = T(3.4)
    gong = np.zeros_like(t)
    for r, a, d in [(1, 1, 2.2), (1.47, 0.5, 1.5), (2.09, 0.4, 1.1), (2.56, 0.3, 0.8), (3.31, 0.2, 0.6)]:
        gong += a * np.sin(2 * np.pi * 73.4 * r * t) * np.exp(-t / d)
    gong *= np.clip(t / 0.004, 0, 1)
    buf = place(buf, 0.7 * gong, 0)
    buf = place(buf, 0.35 * brass(hz(62), 0.7, a=0.08, r=0.3), 0.35)   # D4
    buf = place(buf, 0.35 * brass(hz(59), 1.4, a=0.08, r=0.8), 1.05)   # H3 (fallende kleine Terz)
    drone = (np.sin(2 * np.pi * 36.7 * t) + 0.5 * np.sin(2 * np.pi * 55.1 * t)) * env_adsr(3.4, 1.5, 0.5, 0.8, 1.2)
    buf = place(buf, 0.35 * drone, 0)
    buf = reverb(buf, 0.3, 2.2, 0.7)
    return fades(trim(buf), 0.004, 0.3)


def alarm():
    dur = 2.0
    t = T(dur)
    sel = (np.floor(t / 0.25) % 2).astype(bool)
    f = np.where(sel, 660.0, 880.0)
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = 0.6 * np.sin(ph) + 0.25 * np.sign(np.sin(ph)) + 0.15 * np.sin(3 * ph)
    x = fft_filter(x, hi=4000)
    x *= 0.85 + 0.15 * np.sin(2 * np.pi * 16 * t)
    # weiche Uebergaenge zwischen den Toenen
    gate = 0.85 + 0.15 * np.cos(2 * np.pi * t / 0.25) ** 8
    x *= gate * env_adsr(dur, 0.01, 0.05, 1.0, 0.08)
    return fades(x, 0.003, 0.05)


def horror_drone(L=8.0):
    t = T(L)
    # Frequenzen = Vielfache von 1/L -> exakt periodisch
    def q(f):
        return round(f * L) / L
    x = np.zeros_like(t)
    for f, a in [(55.0, 1.0), (55.375, 0.8), (82.5, 0.5), (110.25, 0.25), (164.875, 0.15)]:
        x += a * np.sin(2 * np.pi * q(f) * t + RNG.uniform(0, 6.28))
    lfo = 0.6 + 0.4 * np.sin(2 * np.pi * t / L)
    x *= lfo
    trit = 0.08 * np.sin(2 * np.pi * q(311.125) * t) * (0.5 - 0.5 * np.cos(2 * np.pi * t / (L / 2))) ** 3
    x += trit
    wind = fft_filter(noise(L), lo=200, hi=900, circular=True)
    wind *= 0.6 + 0.4 * np.sin(2 * np.pi * 2 * t / L + 1)
    x += 0.5 * wind / np.std(wind) * 0.25
    x = reverb(x, 0.35, 3.0, 1.0, circular=True)
    return x


def lofi_loop():
    bpm = 80
    beat = 60 / bpm
    bar = 4 * beat
    L = 4 * bar  # 12 s
    buf = silence(L + 3)
    chords = [[53, 57, 60, 64], [52, 55, 59, 62], [50, 53, 57, 60], [48, 52, 55, 59]]  # Fmaj7 Em7 Dm7 Cmaj7
    roots = [41, 40, 38, 36]
    for b, ch in enumerate(chords):
        st = b * bar
        for m in ch:
            buf = place(buf, 0.16 * epiano(hz(m), bar * 0.95, 0.8), st + RNG.uniform(0, 0.012))
        for m in ch[1:]:
            buf = place(buf, 0.07 * epiano(hz(m + 12), beat, 0.5), st + 2.5 * beat)
        tb = T(bar * 0.9)
        bass = (np.sin(2 * np.pi * hz(roots[b]) * tb) + 0.2 * np.sin(2 * np.pi * hz(roots[b]) * 2 * tb))
        buf = place(buf, 0.35 * bass * env_adsr(bar * 0.9, 0.01, 0.3, 0.6, 0.3), st)
    swing = 0.06
    for k in range(int(L / beat)):
        st = k * beat
        if k % 4 in (0, 2) or (k % 4 == 1 and k % 8 == 5):
            tk = T(0.4)
            kk, _ = sweep(105, 42, tk)
            buf = place(buf, 0.55 * kk * env_exp(tk, 0.13, 0.002), st if k % 4 != 1 else st + beat / 2)
        if k % 4 in (1, 3):
            tn = T(0.25)
            sn = fft_filter(noise(0.25), lo=700, hi=5000) * env_exp(tn, 0.07, 0.001) * 0.25
            sn += 0.12 * np.sin(2 * np.pi * 190 * tn) * env_exp(tn, 0.05)
            buf = place(buf, sn, st)
        for h in (0, 1):
            th = T(0.08)
            hat = fft_filter(noise(0.08), lo=7000) * env_exp(th, 0.018, 0.0005) * (0.08 if h == 0 else 0.05)
            buf = place(buf, hat, st + h * (beat / 2 + swing))
    # Knistern (Vinyl)
    crk = np.zeros(int(L * SR))
    idx = RNG.integers(0, len(crk), 160)
    crk[idx] = RNG.uniform(-1, 1, 160)
    crk = fft_filter(crk, lo=1500, hi=6000, circular=True) * 0.6
    buf[: len(crk)] += crk
    hiss = fft_filter(noise(L), lo=3000, hi=9000, circular=True) * 0.008
    buf[: len(hiss)] += hiss
    loop = fold(buf, L)
    loop = fft_filter(loop, hi=6500, circular=True)  # Lo-Fi-Daempfung
    loop = reverb(loop, 0.15, 1.5, 0.4, circular=True)
    return loop


def wind_loop(L=10.0):
    t = T(L)
    base = fft_filter(noise(L), hi=1200, circular=True, tilt=-0.5)
    gust = 0.55 + 0.3 * np.sin(2 * np.pi * t / L + 0.5) + 0.15 * np.sin(2 * np.pi * 3 * t / L + 2)
    howl = fft_filter(noise(L), lo=350, hi=700, order=4, circular=True)
    howl *= (0.5 + 0.5 * np.sin(2 * np.pi * 2 * t / L)) ** 2
    x = base / np.std(base) * gust + 0.6 * howl / np.std(howl) * gust
    return x


def wasser_loop(L=10.0):
    t = T(L)
    bed = fft_filter(noise(L), lo=300, hi=3500, circular=True, tilt=-0.3)
    bed = bed / np.std(bed) * (0.8 + 0.2 * np.sin(2 * np.pi * 2 * t / L))
    buf = np.concatenate([bed * 0.35, np.zeros(SR)])
    for k in range(140):
        st = RNG.uniform(0, L)
        d = RNG.uniform(0.015, 0.05)
        tb = T(d)
        f0 = RNG.uniform(500, 1400)
        s, _ = sweep(f0, f0 * RNG.uniform(1.5, 2.6), tb)
        buf = place(buf, RNG.uniform(0.05, 0.16) * s * np.sin(np.pi * tb / d), st)
    return fold(buf, L)


def countdown_tick():
    t = T(0.09)
    x = (np.sin(2 * np.pi * 1250 * t) + 0.5 * np.sin(2 * np.pi * 2710 * t)) * env_exp(t, 0.015, 0.0005)
    x += 0.3 * fft_filter(noise(0.09), lo=2000) * np.exp(-t / 0.002)
    return fades(x, 0.0003, 0.015)


def checkpoint():
    buf = silence(0.9)
    buf = place(buf, 0.7 * bell(hz(88), 0.8, 0.4), 0)       # E6
    buf = place(buf, 0.8 * bell(hz(95), 0.9, 0.5), 0.1)     # B6
    for k in range(5):
        buf = place(buf, 0.06 * bell(hz(100 + k * 2), 0.3, 0.1), 0.2 + k * 0.04)
    buf = reverb(buf, 0.2, 1.0, 0.3)
    return fades(trim(buf), 0.001, 0.06)


def sprung():
    t = T(0.2)
    s, f = sweep(240, 720, t)
    x = s * env_adsr(0.2, 0.004, 0.05, 0.7, 0.1)
    x += 0.2 * np.sin(2 * np.pi * np.cumsum(f * 2) / SR) * env_exp(t, 0.05)
    return fades(x, 0.001, 0.03)


SOUNDS = {
    "muenze-pling": lambda: muenze(1.0),
    "muenze-pling-variante-1": lambda: muenze(2 ** (-2 / 12)),
    "muenze-pling-variante-2": lambda: muenze(2 ** (2 / 12)),
    "muenze-pling-variante-3": lambda: muenze(2 ** (4 / 12)),
    "pling-leiter": pling_leiter,
    "pop-klein": pop_klein,
    "ui-klick": ui_klick,
    "ui-oeffnen": lambda: ui_oeffnen(False),
    "ui-schliessen": lambda: ui_oeffnen(True),
    "ui-fehler": ui_fehler,
    "kauf-erfolg": kauf_erfolg,
    "level-up-fanfare": level_up,
    "seltener-drop-mythic": mythic_drop,
    "whoosh-impact": whoosh_impact,
    "treffer-schwer": treffer_schwer,
    "ernte-weich": ernte_weich,
    "wachstum-sparkle": wachstum_sparkle,
    "nacht-beginnt-warnung": nacht_warnung,
    "alarm-diebstahl": alarm,
    "horror-drone-loop": horror_drone,
    "lofi-loop-menue": lofi_loop,
    "ambiente-wind-loop": wind_loop,
    "ambiente-wasser-loop": wasser_loop,
    "countdown-tick": countdown_tick,
    "checkpoint": checkpoint,
    "sprung": sprung,
}

LOOPS = {"horror-drone-loop", "lofi-loop-menue", "ambiente-wind-loop", "ambiente-wasser-loop"}


def write_wav(path, x):
    data = np.clip(np.round(x * 32767), -32768, 32767).astype("<i2")
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(data.tobytes())


def main():
    os.makedirs(ZIEL, exist_ok=True)
    nur = set(sys.argv[1:])
    for name, fn in SOUNDS.items():
        if nur and name not in nur:
            continue
        x = fn()
        x = x - np.mean(x) if name in LOOPS else x
        x = norm(x)
        wav = os.path.join(ZIEL, name + ".wav")
        write_wav(wav, x)
        ogg = os.path.join(ZIEL, name + ".ogg")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-c:a", "libvorbis", "-q:a", "5", ogg], check=True)
        print("%-28s %6.2f s  %s" % (name, len(x) / SR, "(Loop)" if name in LOOPS else ""))


if __name__ == "__main__":
    main()
