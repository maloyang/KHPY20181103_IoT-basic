import dht
from machine import Pin

d = dht.DHT11(Pin(5)) #D1
d.measure()
T = d.temperature() # eg. 23 (℃)
H = d.humidity()    # eg. 41 (% RH)
print("T=%s, H=%s" %(T, H))
