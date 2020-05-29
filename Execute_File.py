import keyboard
import os
shortcut = 'alt+q'

def on_triggered(): #define your function to be executed on hot-key press
    os.system("python final_Call.py")

keyboard.add_hotkey(shortcut, on_triggered)     

keyboard.wait('esc')