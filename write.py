#!/usr/bin/env python3

import argparse
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

parser = argparse.ArgumentParser()
parser.add_argument("text")
args = parser.parse_args()

try:
    print("Place RFID to write \"{}\" to".format(args.text))
    reader.write(args.text)
    print("Written")
finally:
    GPIO.cleanup()
