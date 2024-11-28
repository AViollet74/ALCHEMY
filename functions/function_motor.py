import board
# import RPi.GPIO as GPIO
from time import sleep
from time import monotonic
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit
import gpiod

################################################################################################################################
## Steup I2C communiaciton + base movement
kit = MotorKit(i2c=board.I2C())             #initialises the variable kit to be our I2C Connected Adafruit Motor HAT

def move_up(step_nb):
    """Move the building platform upward by activating the stepper motor in the forward direction
    Args : number of motor rotation step."""

    print("Forward for ", step_nb ,"double steps")

    for i in range(step_nb):
        kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        sleep(0.01)      
    kit.stepper2.release()                  #de-energise the Stepper Motor so it can freely move
################################################################################################################################   
    
    
################################################################################################################################
## MOTOR1 (Z-table)
def move_dist_time_dir_1(distance, temps, sens): #moteur 1 ou 2, distance en mm, temps en secondes, sens en entier positif ou negatif
    """Move the building platform downward, to the starting position (until the photosensor is not reached) by activating the stepper motor in the backrward direction
    Args : GPIO pin number of the photosensor."""
    
    # print(f"Stepper motor moves by {distance}mm in {temps}s, in direction {sens}")
    step_num = round(distance/8*360/1.8)
    sleep_time = temps/step_num
    if sens > 0:
        start_time = monotonic()
        for i in range(step_num):
            kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
                    # Wait for the delay without blocking other processes
            while monotonic() - start_time < sleep_time:
                pass
            start_time=monotonic()
    else :
        start_time = monotonic()
        for i in range(step_num):
            kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
            while monotonic() - start_time < sleep_time:
                pass
            start_time=monotonic()
            
def rotor_no_mvt_1(vitesse, temps, sens): #vitesse en tours par minute, temps en secondes, sens entier positif
    """Moves the motor at a defined speed to disperse particles
    Args : GPIO pin number of the photosensor."""
    
    # print(f"Stepper motor moves at speed {vitesse}rpm during {temps}s, in direction {sens}")
    n_steps_tot=round(vitesse*360/1.8*temps)
    sleep_time=temps/n_steps_tot
    if sens > 0:
        for i in range(n_steps_tot):
            kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
            sleep(sleep_time) 
    else :
        for i in range(n_steps_tot):
            kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
            sleep(sleep_time)
    kit.stepper1.release()

def move_dist_dir_1(distance, sens): #moteur 1 ou 2, distance en mm, temps en secondes, sens en entier positif ou negatif
    """Move the building platform downward, to the starting position (until the photosensor is not reached) by activating the stepper motor in the backrward direction
    Args : GPIO pin number of the photosensor."""
    
    # print(f"Stepper motor moves by {distance}mm, in direction {sens}")
    step_num = round(distance*200/8)
    if sens > 0:
        for i in range(step_num):
            kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
    else :
        for i in range(step_num):
            kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    kit.stepper1.release()

################################################################################################################################
## For MOTOR2 (magnets guide)    
def move_dist_time_dir_2(distance, temps, sens): #moteur 1 ou 2, distance en mm, temps en secondes, sens en entier positif ou negatif
    """Move the building platform downward, to the starting position (until the photosensor is not reached) by activating the stepper motor in the backrward direction
    Args : GPIO pin number of the photosensor."""
    
    # print(f"Stepper motor moves by {distance}mm in {temps}s, in direction {sens}")
    step_num = round(distance/8*360/1.8)
    sleep_time = temps/step_num
    if sens > 0:
        start_time = monotonic()
        for i in range(step_num):
            kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
            while monotonic() - start_time < sleep_time:
                pass
            start_time=monotonic()
    else :
        start_time = monotonic()
        for i in range(step_num):
            kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
            while monotonic() - start_time < sleep_time:
                pass
            start_time=monotonic()
    kit.stepper2.release() 
    
##########################################################    Not used    
def rotor_no_mvt_2(vitesse, temps, sens): #vitesse en tours par minute, temps en secondes, sens entier positif
    """Moves the motor at a defined speed to disperse particles
    Args : GPIO pin number of the photosensor."""
    
    # print(f"Stepper motor moves at speed {vitesse}rpm during {temps}s, in direction {sens}")
    n_steps_tot=round(vitesse*360/1.8*temps)
    sleep_time=temps/n_steps_tot
    if sens > 0:
        for i in range(n_steps_tot):
            kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
            sleep(sleep_time) 
    else :
        for i in range(n_steps_tot):
            kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
            sleep(sleep_time) 
    kit.stepper2.release()
##########################################################      
          
          
            
def move_dist_dir_2(distance, sens): #moteur 1 ou 2, distance en mm, temps en secondes, sens en entier positif ou negatif
    """Move the building platform downward, to the starting position (until the photosensor is not reached) by activating the stepper motor in the backrward direction
    Args : GPIO pin number of the photosensor."""
    
    # print(f"Stepper motor moves by {distance}mm, in direction {sens}")
    step_num = round(distance*200/8)
    if sens > 0:
        for i in range(step_num):
            kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
    else :
        for i in range(step_num):
            kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    kit.stepper2.release()
    
    
## SET initial position 
def start_position_1(sensor_pin):
    """Move the building platform downward, to the starting position (until the photosensor is not reached) by activating the stepper motor in the backrward direction
    Args : GPIO pin number of the photosensor."""
    
    print("Stepper motor goes to start position")
    chip=gpiod.Chip("gpiochip0")
    line=chip.get_line(sensor_pin)
    line.request(consumer="sensor",type=gpiod.LINE_REQ_DIR_IN)
    while line.get_value() == 1:
         kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    kit.stepper1.release()                      #de-energise the Stepper Motor so it can freely move
    print("Start position reached")







"""
#TEST MOTOR
#uncomment the code below to test the photosensor

# The below loop will run 500 times. Each loop it will move one step, clockwise, then pause for 0.01 seconds
# This will almost look like a smooth rotation.

for i in range(500):
    
    print("Forward DOUBLE")
    kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
    sleep(0.01) 


sleep(2) 


# The below loop will run 1000 times. Each loop it will move two step, anti-Clockwise, then pause for 0.01 seconds
# This will almost look like a smooth rotation.

for i in range(500):

    print("Backward DOUBLE")
    kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    sleep(0.01) 

"""