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
    # Author: Meghana, Emma, Sunny (Sigma Team)
    # from TurtleDrive import *from TurtleAttachement import *

    async def runAttachemnt(ta, angle):
        await ta.move_D_angle(angle=angle, speed_percentage=10)


def run_kracken(td, ta):
    # line up is on the middile of the 4rth line (coming from left counting)
    td.set_speed_percentage(speed_percentage=40)
    td.straight_drive(80)
    td.turn(10)
    td.straight_drive(460)
    td.turn(80)
    td.set_speed_percentage(speed_percentage=10)
    td.straight_drive(165)
    td.set_speed_percentage(speed_percentage=2)
    td.straight_drive(85)
    td.straight_drive(-30)
    run_task(runAttachemnt(ta, 118))
    # returning home
    td.set_speed_percentage(speed_percentage=20)
    td.straight_drive(-225)
    td.turn(-60)
    td.set_speed_percentage(speed_percentage=60)
    td.straight_drive(-520)
    run_task(runAttachemnt(ta, -118))
    td.stop()


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_kracken(td, ta)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_kracken(td, ta)
