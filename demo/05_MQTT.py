# demo: push T/H data to MQTT Server

from umqtt.simple import MQTTClient
from machine import Pin
import dht
import ubinascii
import machine
import network
import time
import os

TOPIC_BASE = 'malo-iot'

def dht_get():
    T=None
    H=None
    try:
        d = dht.DHT11(Pin(5)) #D1

        d.measure()
        T = d.temperature()
        H = d.humidity()
    except Exception as e:
        print('dht_get error:', str(e))
    
    return T, H


# Default MQTT server to connect to
server = "iot.eclipse.org"
CLIENT_ID = ubinascii.hexlify(machine.unique_id()).decode('utf-8')
topic_t = TOPIC_BASE+'/T'
topic_h = TOPIC_BASE+'/H'

c = MQTTClient(CLIENT_ID, server)
c.connect()

tm_pub_th = time.ticks_ms()

for i in range(3):
    time.sleep(1)
    T, H = dht_get()
    print("T=%s, H=%s" %(T, H))
    c.publish(topic_t, str(T))
    c.publish(topic_h, str(H))
