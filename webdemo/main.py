# -*- coding: utf-8 -*-

import machine
import network
import time
import os

#- check ap config file
AP_SSID = 'upy'
AP_PWD = 'pypypypy'
ap_config = None
ap_config_fn = 'ap.txt'
if ap_config_fn in os.listdir():
    print('ap config here!')
    f = open(ap_config_fn)
    ap_config = f.read()
    f.close()
if ap_config:
    print( ('ap_config:', ap_config))
    ap_config = ap_config.split('\n')
    AP_SSID = ap_config[0].strip()
    AP_PWD = ap_config[1].strip()
print('line to: ', (AP_SSID, AP_PWD))

#-- 連到AP 為Station
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(AP_SSID, AP_PWD)
sta_if.isconnected()
for i in range(20):
    time.sleep(0.5)
    if sta_if.isconnected():
        break
sta_ip = ''
if sta_if.isconnected():
    print('connected!  --> ', sta_if.ifconfig())
    sta_ip = sta_if.ifconfig()[0]
else:
    print('not connected!  --> ', sta_if.ifconfig())

#-- 當AP，並指定
uid = machine.unique_id()
#ap_if.ifconfig()
# ('192.168.4.1', '255.255.255.0', '192.168.4.1', '192.168.43.1')
# (ip, mask, gateway, dns)
my_sn = '%02X-%02X-%02X' %(uid[0], uid[1], uid[2])

#- Change name/password/ip of ESP8266's AP:
ap_if = network.WLAN(network.AP_IF)
#ap_if.ifconfig([my_ip, my_mask, my_gw, my_dns])

my_ssid = 'up_%s_%s' %(my_sn, sta_ip)
#ap_if.config(essid = my_ssid)#改ssid，馬上生效
ap_if.config(essid=my_ssid, authmode=network.AUTH_WPA_WPA2_PSK, password="12345678")
#DHCP 功能micropython預設就有，不用設定
#AP的IP，每次重開都會回到預設值，因此需要開機時就設定
#一般是配給AP ip的下一號ip


import socket
from machine import Pin
from machine import PWM
import dht


# PIN Define:
D0 = 16
D1 = 5  #PWM
D2 = 4  #PWM
D3 = 0  #PWM
D4 = 2  #PWM, #Led on board
D5 = 14 #PWM
D6 = 12 #PWM
D7 = 13 #PWM
D8 = 15 #PWM

#Setup PINS
led = machine.Pin(2, machine.Pin.OUT)

# th_sensor
th_sensor = dht.DHT11(Pin(D3))

#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 80))
s.listen(5)
while True:
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    '''
    Got a connection from ('10.107.85.22', 64869)
    Content = b'GET /favicon.ico HTTP/1.1\r\nHost: 10.107.85.21\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36\r\nAccept: image/webp,image/apng,image/*,*/*;q=0.8\r\nReferer: http://10.107.85.21/\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7\r\n\r\n'
    '''
    request = str(request)
    led_on = request.find('GET /?LED=ON')
    led_off = request.find('GET /?LED=OFF')
    th_sensor_read = request.find('GET /?th_sensor=read')

    if led_on >= 0:
        print('TURN Led ON')
        led.value(0)
    if led_off >= 0:
        print('TURN Led OFF')
        led.value(1)
    my_t = None
    if th_sensor_read >= 0:
        print('th_sensor read')
        th_sensor.measure()
        my_t = th_sensor.temperature()
        print('T=', th_sensor.temperature())
        print('H=', th_sensor.humidity())

    f = open('webtool.html')

    while(1):
        html = f.read(1024)

        if my_t:
            html = html.replace('T=?degree', 'T=%d degree' %(my_t))
        else:
            html = html.replace('T=?degree', '')

        conn.sendall(html) #改用send all就不會有資料傳一半的問題
        if(len(html)<=0):
            break
    f.close()
    conn.close()
