#!/usr/bin/env python
# -*- coding: utf-8 -*-

import robscreen.constants
from robscreen.core.page import Page


class Acceuil(Page):

    def __init__(self):
        Page.__init__(constants.PAGE_ACCEUIL)

    def print(self, draw):
        draw.text((2, 40), "TEST", font=self.fontb24, fill=O)

    def manage_signals(self, signal):
        if signal == signal.SIGUSR1:
            return constants.PAGE_ACCEUIL
        elif signal == signal.SIGUSR2:
            return constants.PAGE_HELP
        elif signal == signal.SIGUSR3:
            return constants.PAGE_MODE
