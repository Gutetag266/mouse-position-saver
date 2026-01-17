import pyautogui
from pynput import keyboard

print("save kursora (V)")
print("esc - stop programu\n")

def on_press(key):
    try:
        if key.char == 'v':
            x, y = pyautogui.position()
            print(f"Pozycja kursora: ({x}, {y})")
    except AttributeError:
        if key == keyboard.Key.esc:
            print("\n zatrzymano")
            return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()