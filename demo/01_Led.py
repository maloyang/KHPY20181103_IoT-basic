from machine import Pin
import time

led = Pin(2, Pin.OUT) #D4
led.value(0) # ON
for i in range(6):
    led.value(not led.value())
    time.sleep(1)