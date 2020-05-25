import keyboard
import os

shortcut = 'alt+q'
#print('Hotkey set as:', shortcut)

def on_triggered(): #define your function to be executed on hot-key press
    os.system("python final_Call.py 1")
    
keyboard.add_hotkey(shortcut, on_triggered)     

#print("Press ESC to stop.")
keyboard.wait('esc')