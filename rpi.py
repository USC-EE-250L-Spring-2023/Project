import time
import paho.mqtt.client as mqtt
import ssl
import json
import threading
import RPi.GPIO as GPIO
from grovepi import *

dht_sensor_port = 7
dht_sensor_type = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.tls_set(ca_certs='./AmazonRootCA1.pem', certfile='./certificate.pem.crt', keyfile='./private.pem.key', tls_version=ssl.PROTOCOL_SSLv23)
client.tls_insecure_set(True)
client.connect("ao0u04tvflpda-ats.iot.us-east-2.amazonaws.com", 8883, 60)

def intrusionDetector(Dummy):
    while (1):
        [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
        temp = (temp * 9/5) + 32
        heatIndex = -42.379 + (2.04901523 * temp) + (10.14333127 * hum) - (.22475541 * temp * hum) - (.00683783 * temp * temp) - (.05481717 * hum * hum) + (.00122874 * temp * temp * hum) + (.00085282 * temp * hum * hum) - (.00000199 * temp * temp * hum * hum)
        heatIndex = round(heatIndex, 2)
        temppayload = ("Temp = " + str(temp) + "F\tHumidity = " + str(hum) + "%\t " + "Heat Index: " + str(heatIndex) + "F")
        print(temppayload)
        x=GPIO.input(21)
        if (x==0):
            client.publish("device/data", payload=temppayload , qos=0, retain=False)
        time.sleep(5)

intrusion_thread = threading.Thread(target=intrusionDetector, args=("Create intrusion Thread",))

intrusion_thread.start()
client.loop_forever()
