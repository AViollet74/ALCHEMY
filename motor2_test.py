# Below imports all neccessary packages to make this Python Script run
# import time
# import board
# from adafruit_motor import stepper #removed for some reasons
# from adafruit_motorkit import MotorKit
# import functions.function_motor as motor
# import functions.function_photosensor as sensor
from time import sleep
import functions.function_motor2 as motor2


motor2.move_dist_time_dir_dm(32, 1, 1, 1)
sleep(2)
# motor2.move_dist_time_dir_dm(8, 5, -1, 1)
sleep(2)
# motor2.move_dist_time_dir_dm(80, 10, 1, 1)
# sleep(2)
# motor2.move_dist_time_dir_dm(200, 10,1,1)