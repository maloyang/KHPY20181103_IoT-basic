# TODO:量完溫、溼度後，push到line
import urequests

url = "http://khpy-line.herokuapp.com/line"
token = 'YADFITvZVORrWN8rA26VsIJXQBvaGTqPPLgpBfLAYVC'

message =  'KHPY so nice'
message = message.replace(' ', '%20')
payload = {'token':token, "message":message}

#r = urequests.post(url, params=payload) # urequests do not has 'params'
r = urequests.post(url+'?'+'token='+token+'&message='+message)
print('result: ', r.content)
r.close()