from machine import Pin
import time

# 請改為Led以心跳方式閃動
led = Pin(2, Pin.OUT) #D4
led.value(0) # ON
for i in range(6):
    led.value(not led.value())
    time.sleep(1)