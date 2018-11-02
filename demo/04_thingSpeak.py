# demo

import urequests
import dht
from machine import Pin

api_key = 'E2MCZ9NHU3NQ4FXK'
field1 = 20 #T
field2 = 60 #H

url_update = 'http://api.thingspeak.com/update?api_key='+api_key+'&field1='+str(field1)+'&field2='+str(field2)
r = urequests.post(url_update)
print('result: ', r.content)
r.close()
