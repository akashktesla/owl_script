import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Initialize the keyboard
keyboard = Keyboard()

# Give time for the system to recognize the Pico as a keyboard
time.sleep(2)





#simulate keypress example
keyboard.press(Keycode.A)  # Press 'A'
time.sleep(0.1)  # Hold for a short time
keyboard.release(Keycode.A)  # Release 'A'

#/sleep
time.sleep(0.5)  # Wait for a moment

#enter
keyboard.press(Keycode.ENTER)  # Press 'Enter'
time.sleep(0.1)
keyboard.release(Keycode.ENTER)  # Release 'Enter'


# Simulate string
keyboard.write('Hello, this is OwlScript!')

