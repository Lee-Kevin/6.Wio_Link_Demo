# This is a demo by SeeedStudio
import os
from websocket import create_connection
import requests
import json
import time
wio_link_server = "wss://cn.iot.seeed.cc/v1/node/event"
wio_link_key = "your token"
interrupt_n = 13
Wio_link_RedLED = "https://cn.iot.seeed.cc/v1/node/GroveLedWs2812/clear/2/ff0000?access_token=" + wio_link_key
Wio_link_GreenLED = "https://cn.iot.seeed.cc/v1/node/GroveLedWs2812/clear/2/00ff00?access_token=" + wio_link_key
Wio_link_Servo     = "https://cn.iot.seeed.cc/v1/node/GroveServo/angle/10?access_token=" + wio_link_key
Wio_link_Servo1    = "https://cn.iot.seeed.cc/v1/node/GroveServo/angle/90?access_token=" + wio_link_key

ws = create_connection(wio_link_server)
ws.send(wio_link_key)
print "link to Wio Link sensor."

while True:
    requests.post(Wio_link_GreenLED)
    requests.post(Wio_link_Servo1)
    print "Receiving..."

    result = ws.recv()
    json_r = json.loads(result)

    print "Received '%s'" % json_r
    
    print json_r.keys()
    print json_r.get('msg').get('ir_approached')

    if int(json_r.get('msg').get('ir_approached')) == interrupt_n:
        print "Some guys is coming..."
   #    os.system("open /Applications/Mail.app") # for Mac OS 
        os.startfile("D:\Program Files\Foxmail 7.2\Foxmail.exe") # for windows
        requests.post(Wio_link_RedLED)
        requests.post(Wio_link_Servo)
    time.sleep(5)
ws.close()