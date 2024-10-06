# Author: Nitya, Page

from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=20)


def runCoral(td, ta):
    td.set_speed_percentage(50)
    td.straight_drive(670)
    # ta.move_D_time(75, 100)
    run_task(runAttachemnt(ta, -45))
    td.turn(-90)
    td.straight_drive(50)
    run_task(runAttachemnt(ta, 30))
    td.straight_drive(-10)
    td.turn(90)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    # ta.move_D_time(75, 2000)
    runCoral(td, ta)
    # run_task(runAttachemnt(ta))
    # run_task(runCoral(td, ta))
