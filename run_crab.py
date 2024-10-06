# Abby, Elly
from TurtleDrive import *


def runCrab():
    td = TurtleDrive()
    # to drive stright do - td.drive(x mm)
    td.drive(100)


def turn():
    td = TurtleDrive()
    td.drive(325)
    print(td.get_speed)
    td.set_speed(turn_rate=125, turn_acceleration=75)
    td.turn(90)


# runCrab()
turn()
