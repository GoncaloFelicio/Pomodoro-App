# 🍅 Pomodoro App (Python) 🍅

A simple pomodoro app using Python 3.9.2 and pip 24.2, it's also already packaged for MacOS  

What's a pomodoro? --> https://en.wikipedia.org/wiki/Pomodoro_Technique


## How to Use
clone the repo or download the zip from the Github page (hint: green "Code" button)

#### With MacOs 

- via App file:  
The app is already packaged for MacOs, this means after cloning (or unzip) the repo, can go to the folder "*/dist*" and double-click the pomodoro app icon 🍅.  
The app works for my current system: macOS 11.6.4 (20G417), other systems could give an issue.

#### With Python (Mac or Windows)
[Install python](https://www.python.org)
- via python file:  
Can also start the app directly from the python file (this requires using the terminal and having correct python and pip versions).
```sh
cd path/to/repo/Pomodoro-App-main # move to the directory with the app
python3 -m venv venv # create a virtual environment for this app's libraries
source venv/bin/activate # activate the venv just created
pip install -r requirements.txt # install all the requirements
python pomodoro.py # launch the app
```
Should work with the previous code, if there are permissions issue can try adding this to give executable permissions:
```sh
...
chmod +x pomodoro.py # give permisison
python pomodoro.py # launch the app
```

- via jupyter notebook:  
There is also a jupyter notebook in the repo used for development and testing. Can also launch the app by running the first 2 cells:
```sh
cd path/to/repo/Pomodoro_App # move to the directory with the app
python3 -m venv venv # create a venv for this app libraries
source venv/bin/activate # activate the venv just created
pip install -r requirements.txt # install all the requirements
python -m ipykernel install --user --name=venv --display-name "Pomodoro Venv" # add the venv to Jupyter as a kernel
jupyter lab # open jupyter lab
```  
After the Jupyter lab opens can open the file "Pomodoro App testing.ipynb" and run the first cell with code by clicking on the cell and then Shift+Enter.

### If everything works:
- Enjoy!  (˵ •̀ ᴗ - ˵ ) ✧
### else:
- Consider contacting me: goncalo.ag.felicio@gmail.com

---

# To Do's 
( somewhere, sometime in the distant future.. or by the devine grace of a gentle soul that contributes their pen  
૮꒰ ˶• ༝ •˶꒱ა ♡ )

- Package the app to also work on windows,
- Open app by clicking on the terminal executable inside /dist (opens much faster),
- Auto adjust the background image to always match size of the window.

# Final Notes

When packaging the app i first tried with py2app, thats why there's a remnant setup.py file but this did not work, even troubleshooting and trying a lot of fixes did not work in creating a launchable app icon, even though it worked by launching from the terminal executable. Don't know if it has to do with my MacOs version or was doing something else wrong. The build time was also much longer than with pyinstaller, but with pyinstaller i had to adjust the pathing to the resources and add the images and sounds folder manually to the app.
