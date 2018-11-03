import dht
from machine import Pin
import time

d = dht.DHT11(Pin(5)) #D1
led = Pin(2, Pin.OUT) #D4

while(True):
    d.measure()
    T = d.temperature() # eg. 23 (℃)
    H = d.humidity()    # eg. 41 (% RH)
    print("T=%s, H=%s" %(T, H))
    if T>=25:
        led.value(0) #ON
    else:
        led.value(1) #OFF
    time.sleep(1)