from PIL import Image
from PIL import ImageDraw

import time
import signal

from firob.core.worker.worker import Worker
from robscreen import constants
from robscreen.pages.acceuil import Acceuil

import robscreen.core.bakebit_128_64_oled as oled

global instance
instance = None

def receive_signal(signal, stack):
    global instance
    if instance is not None:
        instance.receive_signal(signal)

class Screen(Worker):

    def __init__(self):
        Worker.__init__(self, 0.1)

        oled.init()  # initialze SEEED OLED display
        oled.clearDisplay()  # clear the screen and set start position to top left corner
        oled.setNormalDisplay()  # Set display to normal mode (i.e non-inverse mode)
        oled.setPageMode()  # Set addressing mode to Page Mode

        image = Image.open('resources/firob.png').convert('1')
        oled.drawImage(image)
        
        time.sleep(10)

        self.__page = Acceuil()
        
        
        global instance
        instance = self
        
        signal.signal(signal.SIGUSR1, receive_signal)
        signal.signal(signal.SIGUSR2, receive_signal)
        signal.signal(signal.SIGALRM, receive_signal)


    def execute(self):
        
        image = Image.new('1', (constants.WIDTH, constants.HEIGHT))
        draw = ImageDraw.Draw(image)
        self.__page.print(draw)
        oled.drawImage(image)

    def receive_signal(self, signum):
        page_num = self.__page.manage_signals(signum)
        self.__page = self.newPage(page_num)

    def newPage(self, numero):
        if numero == constants.PAGE_ACCEUIL:
            return Acceuil()
 
