# TODO: 不間斷的量測溫溼度，上傳雲端
import urequests
import dht
from machine import Pin

api_key = 'E2MCZ9NHU3NQ4FXK'

d = dht.DHT11(Pin(5)) #D1
d.measure()
T = d.temperature() # eg. 23 (℃)
H = d.humidity()    # eg. 41 (% RH)
print("T=%s, H=%s" %(T, H))

url_update = 'http://api.thingspeak.com/update?api_key='+api_key+'&field1='+str(T)+'&field2='+str(H)
r = urequests.post(url_update)
print('result: ', r.content)
r.close()
