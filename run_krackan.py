# Author: Meghana, Emma (awesome Team)
#
from TurtleDrive import *
from TurtleAttachement import *


def run_kracken():
    td = TurtleDrive()
    ta = TurtleAttachment()
    # to drive stright do - td.drive(x mm)
    # td.straight_drive(200)
    td.set_speed_percentage(speed_percentage=40)
    td.straight_drive(220)
    td.curve(300, 90)
    td.set_speed_percentage(speed_percentage=50)
    td.straight_drive(20)
    td.set_speed_percentage(speed_percentage=1, acceleration_percentage=1)
    td.straight_drive(55)
    # returning back
    td.straight_drive(-75)
    td.set_speed_percentage(speed_percentage=30)
    td.curve(-300, 90)
    td.set_speed_percentage(speed_percentage=70)
    td.straight_drive(-220)
    td.stop()


if __name__ == "__main__":
    run_kracken()
