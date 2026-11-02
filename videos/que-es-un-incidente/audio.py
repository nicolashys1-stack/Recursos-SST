"""Genera la banda sonora (música + SFX) sincronizada con animacion.html. Salida: WAV estéreo 44.1 kHz."""
import sys, wave, numpy as np
SR, DUR = 44100, 55.0
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
BPM = 112; beat = 60 / BPM
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
music[: int(4 * SR)] *= np.linspace(.35, .7, int(4 * SR))
# silencio dramático alrededor del impacto (9.05 s) y entrada fuerte en el sello
imp = 9.05
g = np.ones(N)
a, c, d = int((imp - .6) * SR), int(imp * SR), int((imp + 1.6) * SR)
g[a:c] = np.linspace(1, .15, c - a); g[c:d] = .15; g[d:int((imp + 2.9) * SR)] = np.linspace(.15, 1, int(1.3 * SR))
music *= g
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

for ts in [4, 12, 17, 25, 32, 40.5, 48]: add(whoosh(), ts - .25, .55)
add(pop(700), .1, .5); add(pop(900), 1.3, .5); add(whoosh(.35), 2.9, .35)
add(creak(), 4 + 3.6, .6)
add(fall_whistle(), 4 + 4.4, 1)
add(crash(), imp, 1.0)
add(pop(1100), imp + 1.3, .5)
add(thud(), 12.85, 1.0)
add(pop(800), 17.05, .4)
for i in range(6): add(pop(600 + i * 80), 17 + 1.0 + i * .45, .25)
add(ding(1046.5), 17 + 4.8, .6); add(ding(1318.5), 17 + 5.2, .6)
add(whoosh(.35), 25.4, .4); add(whoosh(.35), 26.6, .4); add(ding(1568), 28.4, .5)
for i in range(4): add(thud()[: int(.25 * SR)], 32 + .8 + i * .9, .45); add(pop(500 + i * 150), 32 + .8 + i * .9, .3)
add(ding(1760), 37.2, .5)
for i in range(4): add(whoosh(.3), 40.5 + .7 + i * 1.1, .3); add(ding(1318.5 + i * 110), 40.5 + 1.2 + i * 1.1, .55)
add(pop(800), 48.1, .5)
for f, dt in [(1046.5, 0), (1318.5, .12), (1568, .24), (2093, .36)]: add(ding(f), 49.8 + dt, .5)

mix = np.tanh(mix * 1.1) * .89
st = np.stack([mix, mix], 1)
# leve ensanchado estéreo con retardo
st[:, 1] = np.concatenate([np.zeros(220), mix[:-220]]) * .6 + mix * .4
out = (st * 32767).astype(np.int16)
with wave.open(sys.argv[1] if len(sys.argv) > 1 else 'banda_sonora.wav', 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(out.tobytes())
print('ok')
