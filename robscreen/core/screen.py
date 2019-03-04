import time

import robscreen.core.bakebit_128_64_oled as oled

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


from firob.core.worker.worker import Worker
from robscreen.pages.acceuil import Acceuil
from robscreen import constants

class Screen(Worker):

    def __init__(self):
        Worker.__init__(self, 0.1)

        oled.init()                  #initialze SEEED OLED display
        oled.clearDisplay()          #clear the screen and set start position to top left corner
        oled.setNormalDisplay()      #Set display to normal mode (i.e non-inverse mode)
        oled.setPageMode()           #Set addressing mode to Page Mode

        self.width=128
        self.height=64

        time.sleep(10)

        self.__page = Acceuil()

    def execute(self):
        
        image = Image.open('resources/firob.png').convert('1')
        draw = ImageDraw.Draw(image)
        self.__page.print(draw)
        oled.drawImage(image)

    def receive_signal(self, signum, stack):
        page_num = self.__page.manage_signals(signum)
        self.__page = self.newPage(page_num)

    def newPage(self, numero):
        if numero == constants.PAGE_ACCEUIL:
            return Acceuil()
        
        
 
 
