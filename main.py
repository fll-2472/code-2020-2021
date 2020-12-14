#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from drive_tools.p_control import straight_line



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

ev3 = EV3Brick()
right_motor=Motor (Port.C)
left_motor=Motor (Port.D)
right_mission_motor=Motor(Port.A)
left_mission_motor=Motor(Port.B)
gyro = GyroSensor(Port.S3, Direction.COUNTERCLOCKWISE)

drive_base = DriveBase(left_motor, right_motor, 62.4, 15)

straight_line(-42.42, -200, 8000, drive_base, gyro)


