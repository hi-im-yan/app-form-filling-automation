import time
import pyautogui
from coordinates import CELL
from actions import click, type_text, press

pyautogui.FAILSAFE = True

print("Focus the app (5s)...")
time.sleep(5)

click(CELL["A1"])
type_text("Hello world")

click(CELL["B1"])
type_text("I'm being automated")

click(CELL["C1"])
type_text("This is cool")

times_to_tab = 5
print(f"TABBING {times_to_tab} TIMES")
for i in range(times_to_tab):
    press("tab")