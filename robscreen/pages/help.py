#!/usr/bin/env python
# -*- coding: utf-8 -*-

from robscreen import constants
from robscreen.core.page import Page
from robscreen.core.annuaire import Annuaire


class Help(Page):

    def __init__(self):
        Page.__init__(self, Annuaire.PAGE_HELP)

    def draw(self, draw):
                    
        draw.text((15, constants.HEIGHT - 20),    'Help',  font=self.fontb20, fill=255)


    def k1(self):
        return Annuaire.PAGE_ACCEUIL
    def k2(self):
        return Annuaire.PAGE_ACCEUIL
    def k3(self):
        return Annuaire.PAGE_ACCEUIL

