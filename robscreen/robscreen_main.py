#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import signal
import time

from robscreen.core.screen import Screen

from robscreen.pages.acceuil import Acceuil
from robscreen.pages.help import Help
from robscreen.pages.mode import Mode
from robscreen.pages.param import Param
from robscreen.pages.wifi import Wifi


import RPi.GPIO as GPIO

LOGGER = logging.getLogger("firob")

LOGGER.setLevel(logging.DEBUG)

global instance
instance = None

def stop_app(signum, stack):
    if signum == signal.SIGINT :
        print("ByeBye")
        global instance
        instance.stop()
        instance = None
        GPIO.cleanup()

signal.signal(signal.SIGINT, stop_app)

def screen_button(channel):
    if channel == 0 :
        instance.k1()
    elif channel == 2 :
        instance.k2()
    elif channel == 3 :
        instance.k3()

if __name__ == '__main__':
    
    Acceuil()
    Help()
    Mode()
    Param()
    Wifi()
    
    screen = Screen()
    instance = screen
    

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(0, GPIO.IN)
    GPIO.setup(2, GPIO.IN)
    GPIO.setup(3, GPIO.IN)

    GPIO.add_event_detect(0, GPIO.RISING, callback=screen_button, bouncetime=100)
    GPIO.add_event_detect(2, GPIO.RISING, callback=screen_button, bouncetime=100)
    GPIO.add_event_detect(3, GPIO.RISING, callback=screen_button, bouncetime=100)
    
    screen.start()
    while instance is not None:
        time.sleep(0.1)
    screen.join()
    
    
