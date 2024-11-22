# Author: Meghana, Emma, Sunny (Sigma Team)
#
from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=10)


def run_kracken(td, ta):
    # line up is on the middile of the 4rth line (coming from left counting)
    # to drive stright do - td.drive(x mm)
    # td.straight_drive(200)
    td.set_speed_percentage(speed_percentage=40)
    td.straight_drive(80)
    td.turn(10)
    td.straight_drive(445)
    td.turn(80)
    td.set_speed_percentage(speed_percentage=10)
    td.straight_drive(125)
    td.set_speed_percentage(speed_percentage=2)
    td.straight_drive(100)
    td.straight_drive(-45)
    run_task(runAttachemnt(ta, 130))
    # returning home
    td.set_speed_percentage(speed_percentage=10)
    td.curve(-690, 23)
    run_task(runAttachemnt(ta, -118))
    td.stop()


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_kracken(td, ta)
