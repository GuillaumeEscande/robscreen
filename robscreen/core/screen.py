from PIL import Image
from PIL import ImageDraw

import time
import signal

from firob.core.worker.worker import Worker
from robscreen import constants
from robscreen.pages.acceuil import Acceuil

from pkg_resources import resource_filename

import robscreen.core.bakebit_128_64_oled as oled
from robscreen.core.annuaire import Annuaire


class Screen(Worker):

    def __init__(self):
        Worker.__init__(self, 0.1)

        print("Init Screen")
        oled.init()  # initialze SEEED OLED display
        oled.clearDisplay()  # clear the screen and set start position to top left corner
        oled.setNormalDisplay()  # Set display to normal mode (i.e non-inverse mode)
        oled.setHorizontalMode()  # Set addressing mode to Page Mode

        picture = resource_filename('robscreen.resources', 'firob.png')
        image = Image.open(picture).convert('1')
        oled.drawImage(image)
        
        self.__page = Annuaire.getInstance().getPage(Annuaire.PAGE_ACCEUIL)
        
        time.sleep(1)

    def execute(self):
        image = Image.new('1', (constants.WIDTH, constants.HEIGHT))
        draw = ImageDraw.Draw(image)
        self.__page.draw(draw)
        oled.drawImage(image)

    def end(self):
        oled.clearDisplay()
        
    def k1(self):
        page_num = self.__page.k1()
        self.__page = Annuaire.getInstance().getPage(page_num)
    def k2(self):
        page_num = self.__page.k2()
        self.__page = Annuaire.getInstance().getPage(page_num)
    def k3(self):
        page_num = self.__page.k3()
        self.__page = Annuaire.getInstance().getPage(page_num)
 
