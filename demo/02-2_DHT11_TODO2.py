import dht
from machine import Pin
import time

d = dht.DHT11(Pin(5)) #D1

while True:
    d.measure()
    T = d.temperature() # eg. 23 (℃)
    H = d.humidity()    # eg. 41 (% RH)
    print("T=%s, H=%s" %(T, H))

    if T>30:
        ...
    else:
        ...
    time.sleep(1)
    