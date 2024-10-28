# Author: Nitya, Page

from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle, speed):
    await ta.move_D_angle(angle=angle, speed_percentage=speed)


def Deliver_Tree(td, ta):
    # driving into misson model
    run_task(runAttachemnt(ta, 30, 15))
    td.straight_drive(260)
    td.turn(-10)
    td.straight_drive(175)
    td.turn(-20)
    run_task(runAttachemnt(ta, -80, 15))
    td.straight_drive(-100)
    td.turn(50)
    td.straight_drive(-350)


if __name__ == "__main__":
    td = TurtleDrive()
ta = TurtleAttachment()
Deliver_Tree(td, ta)
