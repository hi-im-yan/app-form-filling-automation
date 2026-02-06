import time
import pyautogui
from coordinates import CELL
from actions import click, type_text, press, register_kill_switch, scroll_horizontal
from excel_reader import load_rows, map_row

pyautogui.FAILSAFE = True

register_kill_switch()

print("Move mouse to top left of monitor to cancel at any time")

print("Start reading excel data...")
rows = load_rows("SSD atend.xlsx")
print("Reading complete")

print("Focus the app (5s)...")
time.sleep(3)

for row in rows:
    mapped = map_row(row)
    
    click(CELL["A1"])
    type_text(mapped["service_type"])

    click(CELL["B1"])
    type_text(mapped["schedule_date"])

    click(CELL["C1"])
    type_text(mapped["schedule_time"])

    click(CELL["D1"])
    type_text(mapped["birth_date"])

    press("tab")
    type_text(mapped["establishment"])

    press("tab")
    type_text(mapped["doctor_specialty"])

    press("tab")
    type_text(mapped["doctor_cpf"])

    press("tab")
    type_text(mapped["doctor_cbo"])

    press("tab")
    type_text(mapped["city"])

    press("tab")
    type_text(mapped["zone_type"])

    press("tab")
    type_text(mapped["address"])

    press("tab")
    type_text(mapped["patient_name"])

    press("tab")
    type_text(mapped["patient_cpf"])

    press("tab")
    type_text(mapped["patient_cns"])

    press("tab")
    type_text(mapped["patient_race"])

    press("tab")
    type_text(mapped["phone"])

    press("tab")
    type_text(mapped["cid"])
    
    pyautogui.keyDown("shift")
    pyautogui.scroll(2000)
    pyautogui.keyUp("shift")