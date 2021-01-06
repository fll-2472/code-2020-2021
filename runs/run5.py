from pybricks.ev3devices import (Motor)
from essential.Object_creator import left_mission_motor, right_mission_motor
from essential.Object_creator import right_color_sensor, left_color_sensor
from essential.Object_creator import right_motor, left_motor
from pybricks.tools import wait
from drive_tools.straight_line import straight_line
from essential.Object_creator import drive_base

def run_5():
    straight_line(0, -100, 800, drive_base)
    wait(1000)
    right_mission_motor.dc(-60)
    wait(3000)
    right_mission_motor.dc(50)
    wait(1200)
    right_mission_motor.dc(0)
    straight_line(0, 200, 2000, drive_base)
    wait(10)