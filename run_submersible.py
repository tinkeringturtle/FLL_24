# Anshi, Alice

from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_C_angle(angle=angle, speed_percentage=50)


def run_submersible(td, ta):
    td.set_speed_percentage(speed_percentage=60)
    td.straight_drive(690)
    td.turn(-85)
    td.straight_drive(375)
    td.curve(5, 30)
    td.straight_drive(60)
    td.set_speed_percentage(speed_percentage=100)
    td.curve(10, -90)
    td.straight_drive(50)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_submersible(td, ta)
