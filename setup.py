from setuptools import setup

APP = ['pomodoro.py']  # Your main script

# Data files: images, sounds, and any other resources the app uses
DATA_FILES = [
    ('images', ['images/background.png', 'images/bg1.png']),
    ('sounds', ['sounds/SoulSteal.wav','sounds/DarkMeta.wav',
                'sounds/Impressive.wav','sounds/What.wav',
                'sounds/AsYouWish.wav'])
]

# Options for py2app
OPTIONS = {
    'argv_emulation': True,  # Ensures GUI apps can handle command-line arguments
    'iconfile': 'images/tomato.icns',  # Optional: path to your app's icon
    'includes': ['PIL', 'playsound'],
    'resources': DATA_FILES  # Include data files such as images and sounds
}

# Setup function with metadata
setup(
    name="PomodoroApp",
    version="0.1",
    description="A Castlevania themed Pomodoro timer app for MacOS developed for my own use.",
    author="Gunther Felicio",
    author_email="goncalo.ag.felicio@gmail.com",
    license="MIT",
    keywords="pomodoro pomodoro-timer theme-castlevania macos app",
    url="https://github.com/GoncaloFelicio/Pomodoro-App",
    app=APP,  # Main app entry point
    data_files=DATA_FILES,  # Data files required by the app
    options={'py2app': OPTIONS},  # py2app options
    setup_requires=['py2app'],  # Specify that py2app is required
    classifiers=['Intended Audience :: Science/Research',
                 'Intended Audience :: Developers',
                 'License :: MIT License',
                 "Programming Language :: Python :: 3.9",
                 'Topic :: Software Development',
                 'Topic :: Scientific/Engineering',
                 'Operating System :: MacOS']
)
