import pyautogui
import time

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