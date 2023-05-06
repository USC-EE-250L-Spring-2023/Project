Welcome to our final project!

Team Members:

Charlie Welland
Charlotte Kroll

The files in GitHub need to be compiled in the following two ways. Every file besides GUI.py needs to be cloned into the RPI. Once these files are on the RPI, the only file you need to run on the RPI is RPI.py. This will begin recording data and uploading it to AWS. Before this, you will need a GrovePi and a GrovePi temperature/humidity sensor that is plugged into PORT D7. Once you have the necessary hardware set up, you will run the RPI.py file on your RPI using "python3 RPI.py". This will begin collecting the data and uploading it to AWS. 

Next, on your computer, every file besides RPI.py must be cloned onto your computer. Once these files are on the computer, the only file you need to run is GUI.py. You will run the GUI.py file on your computer using "python3 GUI.py". This will then open a Tkinter window, which will stream the data that is being collected on the RPI. 

We used the following libraries on the RPI:
import time
import paho.mqtt.client as mqtt
import ssl
import json
import threading
import RPi.GPIO as GPIO
from grovepi import *

And the following libraries on the computer:
import ssl
import paho.mqtt.client as mqtt
import tkinter as tk

The link to the video is below:
https://www.youtube.com/watch?v=cvPDFDlu6a0

The write up is EE250 Final Project - Welland_Kroll.pdf this is found in the Repo.
