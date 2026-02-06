import pyautogui
import time
import keyboard
import sys

DEFAULT_DELAY=0.3
LONG_DELAY=2

def click(pos):
    pyautogui.click(pos)
    wait_x_seconds(DEFAULT_DELAY)

def type_text(text):
    pyautogui.write(text, interval=0.05)

def press(key):
    pyautogui.press(key)

def wait_x_seconds(seconds):
    time.sleep(seconds)

def scroll_horizontal(amount):
    pyautogui.keyDown("shift")
    pyautogui.scroll(amount)
    pyautogui.keyUp("shift")
    wait_x_seconds(DEFAULT_DELAY)

def register_kill_switch():
    keyboard.add_hotkey("f12", emergency_exit)

def emergency_exit():
    print("\n🛑 EMERGENCY STOP (F12)")
    sys.exit(1)