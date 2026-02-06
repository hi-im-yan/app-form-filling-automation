# Desktop Automation POC (Python + PyAutoGUI)

This project is a proof of concept (POC) for automating interactions with a desktop application of unknown internals using screen coordinates, keyboard input, and Excel data.  
I made this to help my dad that was needing automation for a manual activity.

### Core Functionality
* **Data Driven:** Reads structured data from an .xlsx file.
* **Safe Formatting:** Maps and formats data safely before input.
* **Direct Interaction:** Interacts with running PC applications via mouse and keyboard emulation.
* **Safety First:** Includes multiple mechanisms to prevent runaway automation.

---

## 🛠 Tech Stack

* **Python 3**
* **PyAutoGUI:** Mouse and keyboard automation.
* **Pandas:** Excel data manipulation.
* **OpenPyXL:** Engine for .xlsx support.
* **Virtualenv:** Environment isolation.

---

## 🚀 Setup

### 1. Create and activate virtual environment
python -m venv venv

# Windows:
venv\Scripts\activate

# Linux / macOS:
source venv/bin/activate

### 2. Install dependencies
pip install -r requirements.txt

> **Note:** On Windows, run the script as Administrator to ensure global hotkeys and input injection work across all application windows.

---

## 🏃 How to Execute

To run the automation successfully, follow these steps:

1. **Prepare Data:** Ensure your `data.xlsx` is in the root/input_files/ directory and follows the expected column schema.
2. **Open Target App:** Launch the desktop application you wish to automate.
3. **Admin Privileges:** Open your terminal or Command Prompt as **Administrator** (required for global hooks).
4. **Run Script:** Execute the entry point:
   ```bash
   python main.py
   ```
5. **Focus Window:** You will have a few seconds of "Startup Delay." Use this time to click on the target application to make it the active window.
6. **Monitor:** Watch the automation proceed. Do not move the mouse or type manually unless you intend to trigger the failsafe.

---

## 🛡 Safety Features

* **PyAutoGUI FAILSAFE:** Slam the mouse cursor into the top-left corner (0,0) of your screen to instantly abort the script.
* **Global Kill Switch (F12):** Press F12 at any time to kill the process, even if the terminal is not the active window.
* **Startup Delay:** The script includes a mandatory pause before execution to allow you to focus the target app or cancel manually.

---

## 📊 Excel Handling

Data integrity is managed through a strict mapping process:
* Excel rows are read via Pandas and converted to dictionaries.
* **Strict String Mapping:** All values (Dates, Times, Numerics) are formatted into strings before reaching the automation layer.
* **Example Mapped Output:**
    * service_type: Teleconsulting
    * schedule_date: 30/01/2026
    * patient_name: Eduardo Costa

---

## ⌨️ Automation Capabilities

* **Precision Clicks:** Mouse interaction at fixed coordinates.
* **Controlled Typing:** Keyboard input with adjustable intervals.
* **Navigation:** TAB-based field switching.
* **Advanced Scrolling:** Vertical/Horizontal scrolling and scrollbar dragging.

---

## 📐 Design Principles

1. Separation of Concerns: UI logic is decoupled from data logic.
2. Stateless Primitives: No business logic inside mouse/keyboard code.
3. Schema Isolation: Excel formatting is handled independently of UI coordinates.
4. Testability: Tools are modular and can be tested in isolation.