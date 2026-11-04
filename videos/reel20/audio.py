"""Reels de 20 s (motor reel20). Genera la banda sonora (música + SFX) sincronizada con animacion.html. Salida: WAV estéreo 44.1 kHz."""
import sys, wave, numpy as np
SR, DUR = 44100, 20.0
N = int(SR * DUR)
rng = np.random.default_rng(7)
mix = np.zeros(N)

def add(sig, t, gain=1.0):
    i = int(t * SR); j = min(N, i + len(sig))
    if i < N: mix[i:j] += sig[: j - i] * gain
def env(n, a=.005, r=None):
    e = np.ones(n); na = max(1, int(a * SR)); e[:na] = np.linspace(0, 1, na)
    if r: e *= np.exp(-np.arange(n) / (r * SR))
    return e
def tone(f, d, wave_='sine'):
    t = np.arange(int(d * SR)) / SR
    if wave_ == 'saw': return 2 * ((t * f) % 1) - 1
    if wave_ == 'sq': return np.sign(np.sin(2 * np.pi * f * t))
    return np.sin(2 * np.pi * f * t)
def lp(x, k=.15):  # filtro pasa-bajos de 1 polo
    y = np.zeros_like(x); acc = 0.
    for i, v in enumerate(x): acc += k * (v - acc); y[i] = acc
    return y

# ---- instrumentos ----
def kick():
    d = .35; t = np.arange(int(d * SR)) / SR
    f = 50 + 110 * np.exp(-t * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9)
def clap():
    n = int(.18 * SR); return rng.standard_normal(n) * env(n, .001, .045) * .6
def hat():
    n = int(.05 * SR); x = rng.standard_normal(n); x = x - np.concatenate([[0], x[:-1]])
    return x * env(n, .001, .012) * .25
def bass(f, d):
    return lp(tone(f, d, 'saw'), .08) * env(int(d * SR), .005, d * .7)
def pluck(f, d=.25):
    return (tone(f, d, 'sq') * .3 + tone(f * 2, d) * .2) * env(int(d * SR), .002, .08)

# ---- música: 112 bpm, Am - F - C - G ----
BPM = 124; beat = 60 / BPM
chords = [(220.0, [440, 523.25, 659.25]), (174.61, [349.23, 440, 523.25]),
          (130.81, [523.25, 659.25, 783.99]), (196.0, [392, 493.88, 587.33])]
music = np.zeros(N)
def madd(sig, t, g):
    i = int(t * SR); j = min(N, i + len(sig))
    if i < N: music[i:j] += sig[: j - i] * g
t = 0.0; b = 0
while t < DUR:
    bar = (b // 4) % 4; root, notes = chords[bar]
    madd(kick(), t, .9)
    if b % 2 == 1: madd(clap(), t, .5)
    madd(hat(), t, .6); madd(hat(), t + beat / 2, .4)
    madd(bass(root / 2, beat * .9), t, .35)
    madd(bass(root / 2, beat * .4), t + beat / 2, .2)
    arp = notes[b % 3] if b % 2 == 0 else notes[(b + 1) % 3]
    madd(pluck(arp), t + beat / 2, .16)
    t += beat; b += 1
# intro (0–4 s): sin bombo, solo tensión
music[: int(2 * SR)] *= np.linspace(.5, .8, int(2 * SR))
fade = int(1.5 * SR); music[-fade:] *= np.linspace(1, 0, fade)
mix += music * .55

# ---- efectos ----
def whoosh(d=.45):
    n = int(d * SR); x = rng.standard_normal(n)
    sweep = np.sin(np.linspace(0, np.pi, n)) ** 2
    k = np.linspace(.02, .35, n); y = np.zeros(n); acc = 0.
    for i in range(n): acc += k[i] * (x[i] - acc); y[i] = acc
    return y * sweep * 1.2
def crash():
    n = int(1.2 * SR); x = rng.standard_normal(n) * env(n, .001, .25)
    return lp(x, .3) * 1.4 + np.pad(kick() * 1.2, (0, n - len(kick())))
def creak(d=.8):
    t = np.arange(int(d * SR)) / SR
    f = 180 + 40 * np.sin(2 * np.pi * 5 * t)
    return lp(np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)), .1) * np.sin(np.pi * t / d) * .5
def thud():
    return np.pad(kick() * 1.4, (0, 2000)) + np.pad(lp(rng.standard_normal(int(.3 * SR)) * env(int(.3 * SR), .001, .06), .2), (0, len(kick()) + 2000 - int(.3 * SR)))
def pop(f=880):
    d = .12; t = np.arange(int(d * SR)) / SR
    return np.sin(2 * np.pi * np.cumsum(f + 900 * np.exp(-t * 40)) / SR) * env(len(t), .001, .03)
def ding(f=1318.5):
    d = .6; return (tone(f, d) + .4 * tone(f * 2.01, d)) * env(int(d * SR), .002, .15) * .5
def fall_whistle(d=.65):
    t = np.arange(int(d * SR)) / SR; f = 1400 - 900 * t / d
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(t), .02) * .22

def stamp():
    return np.pad(kick() * 1.3, (0, 2000))
for ts in [2.6, 7.6, 15]: add(whoosh(), ts - .25, .55)
add(pop(700), .05, .5)
for i in range(3): add(stamp(), .2 + i * .35, .7 + i * .15)
add(crash(), 1.35, .5); add(ding(1318.5), 1.4, .5)
add(pop(800), 2.65, .4); add(pop(1000), 3.2, .45)
for i in range(4): add(pop(600 + i * 90), 2.6 + 1.1 + i * .35, .25)
add(ding(1568), 2.6 + 3.2, .45)
for i in range(3): add(whoosh(.3), 7.6 + .5 + i * 1.9, .3); add(ding(1046.5 + i * 220), 7.6 + .85 + i * 1.9, .55)
for i in range(3): add(stamp(), 15.1 + i * .3, .7)
add(pop(900), 16.3, .45); add(pop(800), 17.1, .5)
for f, dt in [(1046.5, 0), (1318.5, .12), (1568, .24), (2093, .36)]: add(ding(f), 17.6 + dt, .5)

mix = np.tanh(mix * 1.1) * .89
st = np.stack([mix, mix], 1)
# leve ensanchado estéreo con retardo
st[:, 1] = np.concatenate([np.zeros(220), mix[:-220]]) * .6 + mix * .4
out = (st * 32767).astype(np.int16)
with wave.open(sys.argv[1] if len(sys.argv) > 1 else 'banda_sonora.wav', 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(out.tobytes())
print('ok')
