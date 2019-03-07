#!/usr/bin/env python
# -*- coding: utf-8 -*-

from robscreen import constants
from robscreen.core.page import Page
from robscreen.core.annuaire import Annuaire

from pkg_resources import resource_filename
from PIL import Image


class Demo(Page):

    def __init__(self):
        Page.__init__(self, Annuaire.PAGE_MODES_DEMO)

    def draw(self, draw):   
        draw.text((10, 20),    'Demo',  font=self.fontb30, fill=255)

    def k1(self):
        return Annuaire.PAGE_MODES_EXIT
    def k2(self):
        return Annuaire.PAGE_MODE
    def k3(self):
        return Annuaire.PAGE_MODES_EXIT
