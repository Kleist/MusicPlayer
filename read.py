#!/usr/bin/env python3

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    while 1:
        print("Reading")
        id, text = reader.read()
        print("Read:",text)
finally:
    GPIO.cleanup()
