# Pomodoro App

Castlevania-themed Pomodoro timer written in Python and packaged for macOS and Windows.

What it includes:
- configurable work, break, and cycle timers
- custom fonts, images, and sound effects
- standalone packaged builds for macOS and Windows
- a notebook for development and manual testing

## Use

You can run the app in three ways:

### 1. Use a packaged build

macOS:
- unzip `CastleDoroMac.zip`
- open the `CastleDoroMac` folder
- double-click the app bundle inside

Windows:
- unzip `CastleDoroWin.zip`
- open the extracted folder
- double-click the Windows executable

### 2. Run from Python

Install the matching requirements for your platform, then run `pomodoro.py`.

macOS:
```sh
cd /path/to/Pomodoro-App
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirementsMac.txt
python pomodoro.py
```

Windows:
```sh
cd C:\path\to\Pomodoro-App
python -m venv venv
venv\Scripts\activate
pip install -r requirementsWin.txt
python pomodoro.py
```

### 3. Open the testing notebook

The notebook is useful for manual checks and local development.

```sh
python -m ipykernel install --user --name=venv --display-name "Pomodoro Venv"
jupyter lab
```

Open `PomodoroAppTesting.ipynb` and run the notebook cells.

## Requirements

- Python 3.9.x
- platform fonts installed from the `fonts/` folder
- platform-specific packages from `requirementsMac.txt` or `requirementsWin.txt`

## Packaging notes

- macOS packaging works with PyInstaller, but resource paths must be bundled carefully.
- keep the `images/` and `sounds/` folders alongside the packaged app when building locally.
- tkinter needs the custom fonts installed system-wide for the UI to render correctly.

### Packaging command

macOS example:
```sh
pyinstaller --onefile --windowed --name PomodoroApp pomodoro.py
```

Windows example:
```sh
pyinstaller --onefile --windowed --name PomodoroApp --icon=images/tomato_icon_win.ico pomodoro.py
```

If you need bundled assets, keep your packaging script or spec file in sync with the `images/`, `sounds/`, and `fonts/` folders.

For your goal, Tkinter is still the simplest if you want to stay fully in Python and keep the app easy to update.

## Project layout

- `pomodoro.py`: application entry point
- `config.py`: platform-specific UI settings
- `PomodoroAppTesting.ipynb`: development/testing notebook
- `images/`, `sounds/`, `fonts/`: app assets
- `requirementsMac.txt`, `requirementsWin.txt`: platform dependency lists

## Contact

If you run into issues, contact: goncalo.ag.felicio@gmail.com
