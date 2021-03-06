from pybricks.hubs import EV3Brick
from pybricks.parameters import Button
from pybricks.media.ev3dev import SoundFile, ImageFile
import sys
import os
from runs.run1 import run_1
from pybricks.tools import wait
from runs.run2 import run_2
from runs.run3 import run_3
from runs.run4 import run_4
from essential.Object_creator import screen, button, ev3



wait(10)

def run_pick():
    run_number = 1
    while not Button.RIGHT in button.pressed() or Button.LEFT in button.pressed():
        screen.draw_image(0, 0, 'essential/images/run{}.png'.format(run_number))
        while not button.pressed():
            wait(20)
        if Button.DOWN in button.pressed():
            run_number = run_number + 1
            wait(400)
        if Button.UP in button.pressed():
            run_number = run_number - 1
            wait(400)
        if Button.CENTER in button.pressed():
            getattr(sys.modules[__name__], "run_{}".format(run_number))()
            wait(400)
        if run_number >=5:
            run_number = 1
        if run_number <=0:
            run_number = 4
        if button.pressed():
            screen.clear()
            wait(10)
        if Button.RIGHT in button.pressed() or Button.LEFT in button.pressed():
            screen.draw_image(0, 0, 'essential/images/2472end_screen.png')
            wait(2000)
            os._exit(0) 
         
                