# Semester project ALCHEMY
This project aims to build a magnetic- and acoustic-field-assisted 3D printer, by developing software using the Raspberry Pi 400 and Python programming.

## Getting started
1) Activate I2C communication

The Adafruit DC & Stepper Motor HAT requires I2C communication to work. Enable the I2C Connection found under the Interfaces tab in the     Raspberry Pi Configuration menu. **IMPORTANT: Reboot the Raspberry Pi after the modificaiton**

2) Verify the I2C address
   ```bash
   sudo apt-get install i2c-tools
   i2cdetect -y 1
   ```
3) Check the Python version
   ```bash
   python --version
   ```
4) Install pip
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
1) Clone the repository
   ```bash
   git clone git@github.com:mborot/ALCHEMY.git
   ```
2) Install the dependencies
   ```bash
   pip install -r requirements.txt
   ```
3) Test the installation process
   ```bash
   pip list
   ```

## Running the main_1.py script
1) Open the ALCHEMY folder
   ```bash
   cd /Documents/ALCHEMY
   ```
2) Activate the virtual environment
   ```bash
   workon myenv
   ```
The following line should appear in the terminal:
```bash
(myenv)@raspberrypi:$\sim$/Documents/ALCHEMY \$
```
3) Import the image paths
   - Change the folder path
     ```bash
     base\_path = "/home/mborot/Pictures/lattice/"
     ```
   - Change the image names 
     ```bash
     sequence = [base\_path + "cubic\_layer\_0.png", base\_path + "cubic\_layer\_1.png", ...]
     ```
4) Specify the number of layers for each image
   ```bash
   layers = [2, 3, ...]
   ```
5) Specify the layer thickness
   ```bash
   step\_nb = 500
   ```
6) Connect the hardware components to GPIO pins
   
7) Run the code
   ```bash
   python main_1.py
   ```
8) Initialize the hardware elements
   - Number of magnets and piezo elements
   - GPIO pin numbers ([BCM](https://pinout.xyz/) convention)
   - Activation time
   - Frequency
     
9) Close the window
   - At the end of the program: **Esc***
   - While the code is running: **Ctrl + Esc**
   - Stop the code execution in the terminal: **Ctrl + C**


## Running the main_2.py script
3) Import the image paths
   - Change the folder path
     ```bash
     base\_path = "/home/mborot/Pictures/lattice/"
     ```
   - Change the image names 
     ```bash
     sequence = [base\_path + "cubic\_layer\_0.png", base\_path + "cubic\_layer\_1.png", ...]
     ```
4) Specify the number of layers for each image
   ```bash
   layers = [2, 3, ...]
   ```   
7) Run the code
   ```bash
   python main_2.py
   ```
   


## Working with git
1) Check which files have been modified:
```bash
git status
```
2) Add the modified files to your working tree:
```bash
git add script.py
```
3) Commit the changes on the working tree:
```bash
git commit -m "commit message"
```
4) Push your new code on the server:
```bash
git push
```
