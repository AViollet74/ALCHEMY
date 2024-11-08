# Below imports all neccessary packages to make this Python Script run
import time
import board
from adafruit_motor import stepper #removed for some reasons
from adafruit_motorkit import MotorKit
import functions.function_motor as motor
import functions.function_photosensor as sensor
from time import sleep

# Below initialises the variable kit to be our I2C Connected Adafruit Motor HAT
kit = MotorKit(i2c=board.I2C())

sensor_pin = sensor.init_sensor()
print(sensor_pin)


# If you uncomment below it will start by de-energising the Stepper Motor,
# Worth noting the final state the stepper motor is in is what will continue.
# Energised Stepper Motors get HOT over time along with the electronic silicon drivers

# kit.stepper1.release()

# The below loop will run 500 times. Each loop it will move one step, clockwise, then pause for 0.01 seconds
# This will almost look like a smooth rotation.
kit.stepper1.release()
print("Forward SINGLE")
for i in range(200):
    kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)          
    sleep(0.01) 

print("ending 1")



print("moving motor 1 and testing functions2")
motor.move_dist_time_dir_1(20, 10, 1)
print("backwards")
sleep(3)
motor.move_dist_time_dir_1(200, 10, -1)

print("rotor function")
motor.rotor_no_mvt_1(1, 2, 1)
print("faster backwards")
motor.rotor_no_mvt_1(10, 2, -1)
print("stop")
      
sleep(3)

motor.start_position_1(sensor_pin)


# print("moving motor 2 and testing functions")
# motor.move_dist_time_dir_2(20, 10, 1)
# print("back wards")
# motor.move_dist_time_dir_2(200, 10, -1)

# print("rotor function")
# motor.rotor_no_mvt_2(1, 20, 1)
# print("faster")
# motor.rotor_no_mvt_2(10, 20, -1)



# The below loop will run 500 times. Each loop it will move two step, Clockwise, then pause for 0.01 seconds
# This will almost look like a smooth rotation.

# for i in range(500):
#     print("Forward DOUBLE")
#     kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
#     time.sleep(0.01)  


# The below line will de-energise the Stepper Motor so it can freely move
kit.stepper2.release()
