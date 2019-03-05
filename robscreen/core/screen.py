from PIL import Image
from PIL import ImageDraw

import time
import signal

from firob.core.worker.worker import Worker
from robscreen import constants
from robscreen.pages.acceuil import Acceuil

from pkg_resources import resource_filename

import robscreen.core.bakebit_128_64_oled as oled

class Screen(Worker):

    def __init__(self):
        Worker.__init__(self, 1)

        print("Init Screen")
        oled.init()  # initialze SEEED OLED display
        oled.clearDisplay()  # clear the screen and set start position to top left corner
        oled.setNormalDisplay()  # Set display to normal mode (i.e non-inverse mode)
        oled.setHorizontalMode()  # Set addressing mode to Page Mode

        picture = resource_filename('robscreen.resources', 'firob.png')
        image = Image.open(picture).convert('1')
        oled.drawImage(image)
        
        self.__page = Acceuil()
        
        print("Screen Image Draw")
        
        time.sleep(4)



    def execute(self):
        
        print("Screen Execute")
        image = Image.new('1', (constants.WIDTH, constants.HEIGHT))
        draw = ImageDraw.Draw(image)
        self.__page.draw(draw)
        oled.drawImage(image)

    def signal(self, signum):
        page_num = self.__page.manage_signals(signum)
        self.__page = self.newPage(page_num)

    def newPage(self, numero):
        if numero == constants.PAGE_ACCEUIL:
            return Acceuil()
 
