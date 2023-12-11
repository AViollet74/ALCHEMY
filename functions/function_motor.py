import board
import RPi.GPIO as GPIO
from time import sleep
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit


GPIO.setwarnings(False)                     #prevents warnings from showing up when you run the code
GPIO.setmode(GPIO.BCM)                      #BCM = Broadcom chip-specific pin numbers


# Below initialises the variable kit to be our I2C Connected Adafruit Motor HAT
kit = MotorKit(i2c=board.I2C())



def move_up(step_nb):
    print("Forward for ", step_nb ,"double steps")

    for i in range(step_nb):
        kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        sleep(0.01)  
        
    kit.stepper2.release()                  #de-energise the Stepper Motor so it can freely move



def start_position(sensor_pin):

    print("Stepper motor goes to start position")

    while GPIO.input(sensor_pin) == True:
         kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
         sleep(0.01)
    
    kit.stepper2.release()                      #de-energise the Stepper Motor so it can freely move
    print("Start position reached")




"""
#TEST MOTOR

# The below loop will run 500 times. Each loop it will move one step, clockwise, then pause for 0.01 seconds
# This will almost look like a smooth rotation.

for i in range(500):
    
    print("Forward DOUBLE")
    kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
    sleep(0.01) 


sleep(2) 


# The below loop will run 1000 times. Each loop it will move two step, anti-Clockwise, then pause for 0.01 seconds
# This will almost look like a smooth rotation.

for i in range(500):

    print("Backward DOUBLE")
    kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    sleep(0.01) 

"""

