import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

def type_string(text, delay=0.04):
    keycode_map = {
        'a': Keycode.A, 'b': Keycode.B, 'c': Keycode.C, 'd': Keycode.D,
        'e': Keycode.E, 'f': Keycode.F, 'g': Keycode.G, 'h': Keycode.H,
        'i': Keycode.I, 'j': Keycode.J, 'k': Keycode.K, 'l': Keycode.L,
        'm': Keycode.M, 'n': Keycode.N, 'o': Keycode.O, 'p': Keycode.P,
        'q': Keycode.Q, 'r': Keycode.R, 's': Keycode.S, 't': Keycode.T,
        'u': Keycode.U, 'v': Keycode.V, 'w': Keycode.W, 'x': Keycode.X,
        'y': Keycode.Y, 'z': Keycode.Z,
        'A': (Keycode.SHIFT, Keycode.A), 'B': (Keycode.SHIFT, Keycode.B),
        'C': (Keycode.SHIFT, Keycode.C), 'D': (Keycode.SHIFT, Keycode.D),
        'E': (Keycode.SHIFT, Keycode.E), 'F': (Keycode.SHIFT, Keycode.F),
        'G': (Keycode.SHIFT, Keycode.G), 'H': (Keycode.SHIFT, Keycode.H),
        'I': (Keycode.SHIFT, Keycode.I), 'J': (Keycode.SHIFT, Keycode.J),
        'K': (Keycode.SHIFT, Keycode.K), 'L': (Keycode.SHIFT, Keycode.L),
        'M': (Keycode.SHIFT, Keycode.M), 'N': (Keycode.SHIFT, Keycode.N),
        'O': (Keycode.SHIFT, Keycode.O), 'P': (Keycode.SHIFT, Keycode.P),
        'Q': (Keycode.SHIFT, Keycode.Q), 'R': (Keycode.SHIFT, Keycode.R),
        'S': (Keycode.SHIFT, Keycode.S), 'T': (Keycode.SHIFT, Keycode.T),
        'U': (Keycode.SHIFT, Keycode.U), 'V': (Keycode.SHIFT, Keycode.V),
        'W': (Keycode.SHIFT, Keycode.W), 'X': (Keycode.SHIFT, Keycode.X),
        'Y': (Keycode.SHIFT, Keycode.Y), 'Z': (Keycode.SHIFT, Keycode.Z),
        '0': Keycode.ZERO, '1': Keycode.ONE, '2': Keycode.TWO,
        '3': Keycode.THREE, '4': Keycode.FOUR, '5': Keycode.FIVE,
        '6': Keycode.SIX, '7': Keycode.SEVEN, '8': Keycode.EIGHT,
        '9': Keycode.NINE,
        ' ': Keycode.SPACEBAR, '!': (Keycode.SHIFT, Keycode.ONE),
        '@': (Keycode.SHIFT, Keycode.TWO), '#': (Keycode.SHIFT, Keycode.THREE),
        '$': (Keycode.SHIFT, Keycode.FOUR), '%': (Keycode.SHIFT, Keycode.FIVE),
        '^': (Keycode.SHIFT, Keycode.SIX), '&': (Keycode.SHIFT, Keycode.SEVEN),
        '*': (Keycode.SHIFT, Keycode.EIGHT), '(': (Keycode.SHIFT, Keycode.NINE),
        ')': (Keycode.SHIFT, Keycode.ZERO), '-': Keycode.MINUS,
        '_': (Keycode.SHIFT, Keycode.MINUS), '=': Keycode.EQUALS,
        '+': (Keycode.SHIFT, Keycode.EQUALS), '[': Keycode.LEFT_BRACKET,
        '{': (Keycode.SHIFT, Keycode.LEFT_BRACKET), ']': Keycode.RIGHT_BRACKET,
        '}': (Keycode.SHIFT, Keycode.RIGHT_BRACKET), '\\': Keycode.BACKSLASH,
        '|': (Keycode.SHIFT, Keycode.BACKSLASH), ';': Keycode.SEMICOLON,
        ':': (Keycode.SHIFT, Keycode.SEMICOLON), '\'': Keycode.QUOTE,
        '"': (Keycode.SHIFT, Keycode.QUOTE), ',': Keycode.COMMA,
        '<': (Keycode.SHIFT, Keycode.COMMA), '.': Keycode.PERIOD,
        '>': (Keycode.SHIFT, Keycode.PERIOD), '/': Keycode.FORWARD_SLASH,
        '?': (Keycode.SHIFT, Keycode.FORWARD_SLASH), '\n': Keycode.ENTER
    }
    for char in text:
        if char in keycode_map:
            key = keycode_map[char]
            if isinstance(key, tuple):
                keyboard.press(*key)
            else:
                keyboard.press(key)
            keyboard.release_all()
            if delay != 0:
                time.sleep(delay)
                
def key(*keycodes, delay=0.05):
    keyboard.press(*keycodes)
    time.sleep(delay)
    keyboard.release_all()
    time.sleep(delay)

type_string("Hello, World!")