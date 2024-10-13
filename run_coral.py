# Author: Nitya, Page

from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle, speed):
    await ta.move_D_angle(angle=angle, speed_percentage=speed)


def runCoral(td, ta):
    td.set_speed_percentage(50)
    td.straight_drive(665)
    run_task(runAttachemnt(ta, -50, 15))
    td.turn(-85)
    td.straight_drive(60)
    run_task(runAttachemnt(ta, 40, 5))
    td.straight_drive(-10)
    td.turn(90)
    td.straight_drive(40)
    td.turn(-50)
    td.set_speed_percentage(40)
    td.straight_drive(120)
    td.set_speed_percentage(50)
    td.straight_drive(-120)
    td.turn(140)
    td.straight_drive(185)
    td.turn(-95)
    td.straight_drive(40)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    # ta.move_D_time(75, 2000)
    runCoral(td, ta)
    # run_task(runAttachemnt(ta))
    # run_task(runCoral(td, ta))
