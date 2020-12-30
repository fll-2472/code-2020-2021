from pybricks.hubs import EV3Brick
from pybricks.parameters import Button
from pybricks.media.ev3dev import SoundFile, ImageFile
import sys
from runs.run1 import run_1
from pybricks.tools import wait
from runs.run2 import run_2
from runs.run3 import run_3

ev3 = EV3Brick()
button = ev3.buttons
screen = ev3.screen

run_number = 1

wait(10)

def run_pick(left_mission_motor):
    run_number = 1
    while True:
        screen.draw_image(0, 0, 'essential/images/run{}.png'.format(run_number))
        while not button.pressed():
            wait(20)
        if Button.DOWN in button.pressed():
            run_number = run_number + 1
            wait(500)
        if Button.UP in button.pressed():
            run_number = run_number - 1
            wait(500)
        if Button.CENTER in button.pressed():
            getattr(sys.modules[__name__], "run_{}".format(run_number))(left_mission_motor)
            wait(500)
        if run_number >=4:
            run_number = 1
        if run_number <=0:
            run_number = 3
        if button.pressed():
            screen.clear()
        wait(10)
        
        

        