#!/usr/bin/env python3

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

import play
import time


class TagPlayer(object):
    def __init__(self):
        self._current = None
        self.reader = SimpleMFRC522()
        self._failed = 0

    def step(self):
        id, text = self.reader.read_no_block()
        print(id,text)
        if id:
            self._failed = 0
            if text != self._current:
                stripped_text = text.strip()
                print("Read text: \"{}\"".format(stripped_text))
                play.play(stripped_text)
                self._current = text
        elif self._current:
            self._failed += 1
            if self._failed > 2:
                self._current = None
                print("Stopping")
                play.stop()
        time.sleep(1)

def main():
    try:
        player = TagPlayer()
        while 1:
            player.step()
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
