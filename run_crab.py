# Abby, Elly
from TurtleDrive import *


def runCrab():
    td = TurtleDrive()
    # to drive stright do - td.drive(x mm)

    td.curve(200,-45)
    td.set_speed_percentage(speed_percentage=40)
    td.straight_drive(385)
    td.straight_drive(-250)
    td.turn(90)
    td.straight_drive(340)
    td.turn(20)
    td.turn(-90)
    td.set_speed_percentage(speed_percentage=100)
    td.straight_drive(-350)


if __name__ == "__main__":
    runCrab()

