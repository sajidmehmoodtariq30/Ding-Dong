import keyboard
import threading
import os
import sys
from playsound import playsound

def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def play_ting():
    # Plays the sound in a separate thread
    sound_path = get_resource_path("ting.wav")
    try:
        playsound(sound_path)
    except Exception as e:
        print(f"Error playing sound: {e}")
        print(f"Sound path: {sound_path}")
        print(f"File exists: {os.path.exists(sound_path)}")

def on_enter_press(e):
    if e.name == 'enter':
        threading.Thread(target=play_ting, daemon=True).start()

keyboard.on_press(on_enter_press)
keyboard.wait()  # Keeps the script running
