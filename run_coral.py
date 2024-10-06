# Nitya, Page

from TurtleDrive import *


def runCoral():
    td = TurtleDrive()
    # to drive stright do - td.drive(x mm)
    td.straight_drive(100)


def turn():
    td = TurtleDrive()
    td.straight_drive(325)
    print(td.get_speed)
    td.set_speed(turn_rate=125, turn_acceleration=75)
    td.turn(90)


runCoral()
turn()
