import functions.function_photosensor as sensor
from gpiozero import Button
from time import sleep

# Initialize the sensor pin
sensor_pin = sensor.init_sensor()
print(sensor_pin)

# Set up the sensor as a Button (input pin)
sensor_button = Button(sensor_pin)

print("Photo sensor setup success")

while True:
    # Read the value from the sensor pin
    if sensor_button.is_pressed:
        print("Sensor triggered (HIGH)")
    else:
        print("Sensor not triggered (LOW)")
    
    sleep(0.25)