# Anshi, Alice

from TurtleDrive import *
from TurtleAttachement import *


def run_whale():
    td = TurtleDrive()
    ta = TurtleAttachment()
    #
    td.striaght_drive(100)
    td.curve(angle=30, radius=5)
    ta.move_c_angle(10)
    td.set_speed_percentage(100)
    td.curve(-30)
    td.straight_drive(100)


if __name__ == "__main__":
    run_whale()
