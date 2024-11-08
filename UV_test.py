import functions.function_UV as uv
from time import sleep
uv_pin = uv.init_uv()
print("UV light setup success")

while True:
    uv.switch_on(uv_pin)
    sleep(4)
    uv.switch_off(uv_pin)
    sleep(4)












