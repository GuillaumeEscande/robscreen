#!/usr/bin/env python
# -*- coding: utf-8 -*-

from robscreen import constants
from robscreen.core.page import Page
from robscreen.core.annuaire import Annuaire

from pkg_resources import resource_filename
from PIL import Image


class Acceuil(Page):

    def __init__(self):
        Page.__init__(self, Annuaire.PAGE_ACCEUIL)

    def draw(self, draw):

        picture = resource_filename('robscreen.resources', 'home.png')
        image = Image.open(picture).convert('1')
        draw.bitmap(((constants.WIDTH - 40)/2, 5), image, fill=255)                
        draw.text(((constants.WIDTH - 6*14)/2, constants.HEIGHT - 20),    'Acceuil',  font=self.fontb20, fill=255)


    def k1(self):
        return Annuaire.PAGE_WIFI
    def k2(self):
        return Annuaire.PAGE_HELP
    def k3(self):
        return Annuaire.PAGE_MODE

