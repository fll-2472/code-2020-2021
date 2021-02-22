from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#Add more obgect only here enless there
ev3 = EV3Brick()
button = ev3.buttons
screen = ev3.screen
right_motor = Motor(Port.C)
left_motor =Motor(Port.D)
right_mission_motor = Motor(Port.A)
left_mission_motor = Motor(Port.B)
gyro = GyroSensor(Port.S3, Direction.COUNTERCLOCKWISE)
left_color_sensor = ColorSensor(Port.S4)
right_color_sensor = ColorSensor(Port.S1)
drive_base = DriveBase(left_motor, right_motor, 62.4, 15)

