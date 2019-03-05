#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import signal
import time

from robscreen.core.screen import Screen

LOGGER = logging.getLogger("firob")

LOGGER.setLevel(logging.DEBUG)


instance = None

def receive_signal(signal, stack):
    print("TEST 01")
    if instance is not None:
        print("TEST 02")
        instance.signal(signal)


if __name__ == '__main__':
    screen = Screen()
    
    instance = screen
        
    signal.signal(signal.SIGUSR1, receive_signal)
    signal.signal(signal.SIGUSR2, receive_signal)
    signal.signal(signal.SIGALRM, receive_signal)
    
    screen.start()
    while 1:
        time.sleep(0.1)
    
    
