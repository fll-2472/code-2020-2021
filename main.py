#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from drive_tools.straight_line import straight_line
from drive_tools.turn import turn
from drive_tools.follow_line import follow_line

ev3 = EV3Brick()
right_motor = Motor(Port.C)
left_motor =Motor(Port.D)
right_mission_motor = Motor(Port.A)
left_mission_motor = Motor(Port.B)
gyro = GyroSensor(Port.S3, Direction.COUNTERCLOCKWISE)
left_color_sensor = ColorSensor(Port.S4)
right_color_sensor = ColorSensor(Port.S1)
drive_base = DriveBase(left_motor, right_motor, 62.4, 15)


follow_line(-200, 5000, drive_base, right_color_sensor)