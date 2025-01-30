# pico_hid | USB HID Keyboard Emulator

This Python script emulates a USB keyboard using CircuitPython and the Adafruit HID library. It allows automated keystroke input, including typing full strings with customizable delays.

## Features
- Emulates a USB keyboard
- Supports typing full strings with adjustable delays
- Supports special character inputs
- Provides a function to press arbitrary key combinations

## Requirements
- A microcontroller board that supports USB HID (e.g., Raspberry Pi Pico, Adafruit Trinket M0, etc.)
- CircuitPython installed on the board
- `adafruit_hid` library installed

## Installation
1. Install CircuitPython on your microcontroller board.
2. Download and copy the `adafruit_hid` library into the `lib/` folder on your board.
3. Save the script as `code.py` on your microcontroller board.

## Usage

### Type a String
Use the `type_string` function to simulate typing a string.
```python
from your_script_name import type_string

type_string("Hello, World!")
```

### Press Key Combinations
Use the `key` function to press and release keys with a delay.
```python
from adafruit_hid.keycode import Keycode
from your_script_name import key

key(Keycode.CONTROL, Keycode.C)  # Simulates Ctrl+C
```

## Example Code
```python
type_string("Hello, World!")
```

## License
This project is licensed under the unlicense.

## Contributing
Pull requests are welcome! Feel free to open an issue if you find a bug or have a feature request.

## Acknowledgments
- [Adafruit HID Library](https://github.com/adafruit/Adafruit_CircuitPython_HID)
- CircuitPython community

