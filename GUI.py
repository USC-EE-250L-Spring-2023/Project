import ssl
import paho.mqtt.client as mqtt
import tkinter as tk

# Define MQTT parameters
iot_endpoint = "ao0u04tvflpda-ats.iot.us-east-2.amazonaws.com"
ca_path = "/Users/charliewelland/desktop/MQTT/AmazonRootCA1.pem"
cert_path = "/Users/charliewelland/desktop/MQTT/certificate.pem.crt"
key_path = "/Users/charliewelland/desktop/MQTT/private.pem.key"
topic = "device/data"

# Define callback function for when a message is received
def on_message(client, userdata, message):
    message_text = message.payload.decode()
    label2.config(text=message_text)

# Create MQTT client object
client = mqtt.Client()
client.tls_set(ca_certs=ca_path, certfile=cert_path, keyfile=key_path, 
               cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2)

# Set callback function
client.on_message = on_message

# Connect to AWS IoT Core
client.connect(iot_endpoint, port=8883)

# Subscribe to topic
client.subscribe(topic)

# Create a tkinter window with two labels
root = tk.Tk()
root.title('MQTT Messages')
root.geometry('1280x720')
root.configure(bg='white')


label1 = tk.Label(root, text='WEATHER INFO:', font=('Arial', 20), bg='white')
label1.place(relx=0.5, rely=0.47, anchor='center')

label2 = tk.Label(root, font=('Arial', 16), bg='white')
label2.place(relx=0.5, rely=0.53, anchor='center')

# Start loop to receive messages
client.loop_start()

# Run the tkinter event loop
root.mainloop()

# Stop MQTT client loop when the tkinter window is closed
client.loop_stop()
