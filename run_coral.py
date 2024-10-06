# Author: Nitya, Page

from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta):
    await ta.move_D_angle(angle=160, speed_percentage=20)
    await ta.move_D_angle(angle=-160, speed_percentage=20)


def runCoral(td, ta):
    td.set_speed_percentage(50)
    td.straight_drive(660)
    run_task(runAttachemnt(ta))
    td.turn(-90)
    td.straight_drive(50)
    td.straight_drive(-10)
    td.turn(90)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    runCoral(td, ta)
    # run_task(runAttachemnt(ta))
    # run_task(runCoral(td, ta))
