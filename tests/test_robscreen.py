#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import unittest
from unittest.mock import MagicMock
from unittest.mock import Mock

import sys

from robscreen.core.screen import Screen

class TestScreen(unittest.TestCase):

    def test(self):
        screen = Screen()
        screen.start()
        screen.join()
                
if __name__ == "__main__":
    unittest.main()
