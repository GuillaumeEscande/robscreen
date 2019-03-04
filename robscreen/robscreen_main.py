#!/usr/bin/env python
# -*- coding: utf-8 -*-


from robscreen.core.screen import Screen

import logging
LOGGER = logging.getLogger("firob")

LOGGER.setLevel(logging.DEBUG)

if __name__ == '__main__':
    screen = Screen()
    screen.start()
    screen.join()
    