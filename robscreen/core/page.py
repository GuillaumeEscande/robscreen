#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import ImageFont
from robscreen.core.annuaire import Annuaire

from pkg_resources import resource_filename

class Page():

    def __init__(self, identifier):
        self.font = ImageFont.load_default()
        font_file = resource_filename('robscreen.resources', 'DejaVuSansMono.ttf')
        self.fontb20 = ImageFont.truetype(font_file, 20)
        self.__id = identifier
        Annuaire.getInstance().addPage(self.__id, self)

    def draw(self, draw):
        pass

    def k1(self):
        pass
    def k2(self):
        pass
    def k3(self):
        pass

    @property
    def id(self):
        return self.__id
