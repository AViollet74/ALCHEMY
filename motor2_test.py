from time import sleep
import functions.function_motor2 as motor2
ID=1

motor2.move_dist_time_dir_dm(24, 5, 1, ID)
sleep(2)
print("2e partei")
motor2.move_dist_time_dir_dm(24, 5, -1, ID)


ID=2

motor2.move_dist_time_dir_dm(24, 5, 1, ID)
sleep(2)
print("2e partei")
motor2.move_dist_time_dir_dm(24, 5, -1, ID)
# motor2.move_dist_time_dir_dm(8, 5, -1, 1)
# sleep(2)
# motor2.move_dist_time_dir_dm(80, 10, 1, 1)
# sleep(2)
# motor2.move_dist_time_dir_dm(200, 10,1,1)