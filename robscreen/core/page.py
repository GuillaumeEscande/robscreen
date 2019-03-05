#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import ImageFont


class Page():

    def __init__(self, identifier):
        self.font = ImageFont.load_default()
        self.fontb24 = ImageFont.truetype('resources/DejaVuSansMono-Bold.ttf', 24)
        self.__id = identifier

    def draw(self, draw):
        pass

    def manage_signals(self, signal):
        pass

    @property
    def id(self):
        return self.__id
