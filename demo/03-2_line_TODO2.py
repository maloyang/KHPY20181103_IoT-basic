# 示範解題: 當溫度超過30度時，發出警告訊息
import dht
from machine import Pin
import urequests
import time

def send_line(token = 'YADFITvZVORrWN8rA26VsIJXQBvaGTqPPLgpBfLAYVC', message =  'KHPY so nice...'):
    url = "http://khpy-line.herokuapp.com/line2"
    payload = {'token':token, "message":message}
    r = urequests.post(url, json=payload) #not real json data to server, it use 'data'
    print('result: ', r.content)
    r.close()


d = dht.DHT11(Pin(5)) #D1

while(True):
    d.measure()
    T = d.temperature() # eg. 23 (℃)
    H = d.humidity()    # eg. 41 (% RH)
    print("T=%s, H=%s" %(T, H))
    if T>=32:
        send_line(message='temperature high alarm!! (%d)' %(T))
        time.sleep(5)
    time.sleep(1)