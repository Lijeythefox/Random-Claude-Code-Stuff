import math
import random
from machine import Pin
import neopixel
from PiicoDev_Potentiometer import PiicoDev_Potentiometer
from PiicoDev_Unified import sleep_ms

LED_PIN = 0
NUM_LEDS = 30
BRIGHTNESS = 0.5
FRAME_MS = 16

SMOOTHING = 0.12
LUT_SIZE = 64
TAU = 2 * math.pi

PALETTES = [
    [(0, 8, 50), (0, 60, 160), (0, 190, 210), (120, 255, 240)],
    [(0, 70, 30), (0, 210, 110), (40, 60, 220), (170, 0, 190)],
    [(70, 0, 130), (210, 0, 130), (255, 70, 30), (255, 170, 40)],
    [(140, 0, 0), (255, 40, 0), (255, 130, 0), (255, 230, 90)],
    [(255, 0, 60), (255, 200, 0), (0, 255, 120), (80, 0, 255)],
]


def lerp(a, b, t):
    return a + (b - a) * t


def lerp_rgb(c1, c2, t):
    return (lerp(c1[0], c2[0], t), lerp(c1[1], c2[1], t), lerp(c1[2], c2[2], t))


def smoothstep(t):
    return t * t * (3 - 2 * t)


def sample_palette(palette, x):
    pos = (x % 1.0) * len(palette)
    i = int(pos)
    blend = smoothstep(pos - i)
    return lerp_rgb(palette[i], palette[(i + 1) % len(palette)], blend)


def build_lut(mood):
    pos = mood * (len(PALETTES) - 1)
    i = min(int(pos), len(PALETTES) - 2)
    blend = smoothstep(pos - i)
    lut = []
    for k in range(LUT_SIZE):
        x = k / LUT_SIZE
        lut.append(lerp_rgb(sample_palette(PALETTES[i], x), sample_palette(PALETTES[i + 1], x), blend))
    return lut


def read_mood(pot):
    return max(0.0, min(1.0, pot.value / 100))


def main():
    pot = PiicoDev_Potentiometer(minimum=0, maximum=100)
    strip = neopixel.NeoPixel(Pin(LED_PIN), NUM_LEDS)

    mood = read_mood(pot)
    previous_mood = mood
    lut_mood = mood
    lut = build_lut(mood)

    energy = 0.0
    phase = 0.0
    comet = 0.0
    sparkles = [0.0] * NUM_LEDS

    while True:
        mood += (read_mood(pot) - mood) * SMOOTHING
        energy = min(1.0, energy * 0.9 + abs(mood - previous_mood) * 40)
        previous_mood = mood

        if abs(mood - lut_mood) > 0.003:
            lut = build_lut(mood)
            lut_mood = mood

        speed = 0.02 + mood * 0.1 + energy * 0.25
        phase += speed
        comet = (comet + speed * 6) % NUM_LEDS
        tail = 3 + mood * 8 + energy * 6

        if random.random() < 0.04 + energy * 0.9:
            sparkles[random.randrange(NUM_LEDS)] = 1.0

        for i in range(NUM_LEDS):
            x = i / NUM_LEDS
            wave = math.sin(x * TAU * 1.5 + phase) + math.sin(x * TAU * 0.7 - phase * 0.6 + 1.3)
            index = int((wave * 0.25 + 0.5 + phase * 0.03) * LUT_SIZE) % LUT_SIZE
            r, g, b = lut[index]

            pulse = 0.5 + 0.5 * math.sin(x * TAU * 2 - phase * 1.3)
            level = 0.15 + 0.6 * pulse * pulse

            behind = (comet - i) % NUM_LEDS
            if behind < tail:
                glow = 1 - behind / tail
                level += glow * glow * 0.9

            level = min(level, 1.0)
            r, g, b = r * level, g * level, b * level

            sparkle = sparkles[i]
            if sparkle > 0.01:
                r = lerp(r, 255, sparkle)
                g = lerp(g, 255, sparkle)
                b = lerp(b, 255, sparkle)
                sparkles[i] = sparkle * 0.78
            else:
                sparkles[i] = 0.0

            strip[i] = (int(r * BRIGHTNESS), int(g * BRIGHTNESS), int(b * BRIGHTNESS))

        strip.write()
        sleep_ms(FRAME_MS)


main()
