# Semester project ALCHEMY
This project aims to build a magnetic- and acoustic-field-assisted 3D printer, by developing software using the Raspberry Pi 400 and Python programming.

## Getting started
1) Activate I2C communication
   The Adafruit DC & Stepper Motor HAT requires I2C communication to work. Enable the I2C Connection found under the Interfaces tab in the     Raspberry Pi Configuration menu
2) Reboot the Raspberry Pi
3) Verify the I2C address
   ```bash
   sudo apt-get install i2c-tools
   i2cdetect -y 1
   ```
4) Check the Python version
   ```bash
   python --version
   ```
5) Install pip
   ```bash
   sudo apt-get install python-pip
   ```
## Create a virtual environment
1) Install virtualenvwrapper
   ```bash
   sudo pip install virtualenvwrapper
   ```
2) Configure the shell to load the virtualenvwrapper commands
   - Open an RC file (e.g. .bashrc, .bash\_profile, or .zshrc)
     ```bash
     sudo gedit ~/.bashrc
     ```
   - Add the following lines
     ```bash
     export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
     export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
     source /usr/local/bin/virtualenvwrapper.sh
     ```
   - Save the file
3) Check the virtualenvwrapper version
   ```bash
   mkvirtualenv --version
   ```
4) Create a new environment
   ```bash
   mkvirtualenv myenv
   ```
5) Activate the virtual environment
   ```bash
   workon myenv
   ```
6) Deactivate the virtual environment
   ```bash
   (myenv) deactivate
   ```
7) List virtual environments
   ```bash
   lsvirtualenv
   ```
8) List the packages in the virtual environment
   ```bash
   pip freeze
   ```
9) Remove the virtual environment
   ```bash
   rmvirtualenv myenv
   ```

## Installation



## Work on your project
1) Activate the environement
```bash
workon ALCHEMY
```
2) If you want to deactivate the environnement
```bash
deactivate
```
3) To list all the current module on the environnement
```bash
pip freeze
```
## Installation
- Clone the repo

```bash
git clone git@github.com:mborot/ALCHEMY.git
```
- Create your virtual env
```bash
mkvirtualenv ALCHEMY
```



## Managing dependancies
- to add an dependancy with poetry for exemple numpy
```bash
poetry add numpy
```
It would automatically install and udpate the pyproject.toml file. If you didn't specifie it, it would add it to the tool.poetry.dependencies.


## Working with git
1) Check wich files have been modified:
```bash
git status
```
2) Add the modified files to your working tree:
```bash
git add script.py
```
3) Commit the changes on the working tree:
```bash
git commit -m "update_2.0"
```
4) Push your new code on the server:
```bash
git push
```
If you have any issues: 1) Read the error and google it 2) Use git status to ensure that all the modified files have been save 3) Cry if you see the error conflict.
