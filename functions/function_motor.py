import board
import RPi.GPIO as GPIO
from time import sleep
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit


#GPIO settings
GPIO.setwarnings(False)                     #prevents warnings from showing up when you run the code
GPIO.setmode(GPIO.BCM)                      #BCM = Broadcom chip-specific pin numbers


kit = MotorKit(i2c=board.I2C())             #initialises the variable kit to be our I2C Connected Adafruit Motor HAT


def move_up(step_nb):
    """Move the building platform upward by activating the stepper motor in the forward direction
    Args : number of motor rotation step."""

    print("Forward for ", step_nb ,"double steps")

    for i in range(step_nb):
        kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        sleep(0.01)  
        
    kit.stepper2.release()                  #de-energise the Stepper Motor so it can freely move



def start_position(sensor_pin):
    """Move the building platform downward, to the starting position (until the photosensor is not reached) by activating the stepper motor in the backrward direction
    Args : GPIO pin number of the photosensor."""

    print("Stepper motor goes to start position")

    while GPIO.input(sensor_pin) == True:
         kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
         sleep(0.01)
    
    kit.stepper2.release()                      #de-energise the Stepper Motor so it can freely move
    print("Start position reached")




"""
#TEST MOTOR
#uncomment the code below to test the photosensor

# The below loop will run 500 times. Each loop it will move one step, clockwise, then pause for 0.01 seconds
# This will almost look like a smooth rotation.

for i in range(500):
    
    print("Forward SINGLE")
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