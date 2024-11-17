# Author: Nitya, Page

from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle, speed):
    await ta.move_D_angle(angle=angle, speed_percentage=speed)


def Deliver_Tree(td, ta):
    # driving into misson model
    run_task(runAttachemnt(ta, 30, 15))
    td.straight_drive(450)
    ta.move_D_time(speed_percentage=20, time_millisec=200)
    run_task(ta.move_C_angle(angle=-50, speed_percentage=15))
    # run_task(ta.move_C_angle(angle=3, speed_percentage=15))
    td.straight_drive(-450)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    Deliver_Tree(td, ta)
