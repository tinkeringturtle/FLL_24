# Anshi, Alice

from TurtleDrive import *
from TurtleAttachement import *


def run_whale():
    td = TurtleDrive()
    ta = TurtleAttachment()

    td.set_speed_percentage(speed_percentage=60)
    td.straight_drive(685)
    td.turn(45)
    td.straight_drive(180)
    ta.move_C_angle(200)
    # td.curve(angle=30, radius=5)
    # ta.move_c_angle(10)
    # td.set_speed_percentage(100)
    # td.curve(-30)
    # td.straight_drive(100)""


# if __name__ == "__main__":
run_whale()
