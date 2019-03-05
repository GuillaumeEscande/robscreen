#!/usr/bin/env python
# -*- coding: utf-8 -*-

from robscreen import constants
from robscreen.core.page import Page


class Acceuil(Page):

    def __init__(self):
        Page.__init__(self, constants.PAGE_ACCEUIL)

    def draw(self, draw):
        
        print("Acceuil draw")
        draw.rectangle((0,0,constants.WIDTH,constants.HEIGHT), outline=0, fill=0)
        
        # Draw some shapes.
        # First define some constants to allow easy resizing of shapes.
        padding = 2
        shape_width = 20
        top = padding
        bottom = constants.HEIGHT-padding
        # Move left to right keeping track of the current x position for drawing shapes.
        x = padding
        # Draw an ellipse.
        draw.ellipse((x, top , x+shape_width, bottom), outline=255, fill=0)
        x += shape_width+padding
        # Draw a rectangle.
        draw.rectangle((x, top, x+shape_width, bottom), outline=255, fill=0)
        x += shape_width+padding
        # Draw a triangle.
        draw.polygon([(x, bottom), (x+shape_width/2, top), (x+shape_width, bottom)], outline=255, fill=0)
        x += shape_width+padding
        # Draw an X.
        draw.line((x, bottom, x+shape_width, top), fill=255)
        draw.line((x, top, x+shape_width, bottom), fill=255)
        x += shape_width+padding

        
        
        draw.text((x, top),    'Hello',  font=self.font, fill=255)
        draw.text((x, top+20), 'World!', font=self.font, fill=255)

    def manage_signals(self, signal):
        print("Acceuil manage_signals " + str(signal))
        if signal == signal.SIGUSR1:
            return constants.PAGE_ACCEUIL
        elif signal == signal.SIGUSR2:
            return constants.PAGE_HELP
        elif signal == signal.SIGUSR3:
            return constants.PAGE_MODE
