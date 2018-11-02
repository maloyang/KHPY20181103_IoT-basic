esptool.py --port com4 erase_flash

esptool.py --port com4 --baud 460800 write_flash --flash_size=detect -fm dio 0 esp8266-20180511-v1.9.4.bin