from micropyserver import MicroPyServer
from machine import Pin
from time import sleep
import dht, ujson, network, esp

sensor = dht.DHT22(Pin(<YourPin>))


''' Код подключения к WiFi '''
wlan_id = "<SSID>"
wlan_pass = "<Password>"


def GetData():
  try:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    return ujson.dumps({"success":True,
            "temp":temp,
            "humidity":hum})
  except:
    return ujson.dumps({"success":False,
            "temp":None,
            "humidity":None})




wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if wlan.isconnected() == False:
    wlan.connect(wlan_id, wlan_pass)
    while wlan.isconnected() == False:
        sleep(1)

def show_message(request):
    server.send("HTTP/1.0 200 OK\r\n")
    server.send("Content-Type: application/json\r\n\r\n")
    
    server.send(str(GetData()))

server = MicroPyServer()
server.add_route("/", show_message)
server.start()
