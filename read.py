#!/usr/bin/env python3

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from .play import play

reader = SimpleMFRC522()

while 1:
    print("Reading")
    id, text = reader.read()
    print("Read:",text)
    play(text)
finally:
    GPIO.cleanup()
