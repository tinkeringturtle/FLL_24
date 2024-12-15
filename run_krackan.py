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
        await ta.move_D_angle(angle=angle, speed_percentage=30)


def run_kracken(td, ta):
    # line up is on the middile of the 4rth line (coming from left counting)
    td.set_speed_percentage(speed_percentage=40, acceleration_percentage=35)

    td.straight_drive(80)
    td.turn(10)
    td.straight_drive(460)
    td.turn(80)
    td.set_speed_percentage(speed_percentage=10, acceleration_percentage=10)
    td.straight_drive(125)
    td.set_speed_percentage(speed_percentage=5, acceleration_percentage=5)
    td.straight_drive(78)
    td.straight_drive(-45)
    run_task(runAttachemnt(ta.move_C_angle(30))(ta, 118))
    # returning home
    td.set_speed_percentage(speed_percentage=20, acceleration_percentage=15)
    td.straight_drive(-225)
    td.turn(-90)
    td.set_speed_percentage(speed_percentage=65, acceleration_percentage=60)
    td.straight_drive(-520)
    td.turn(-95)
    td.stop()


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_kracken(td, ta)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_kracken(td, ta)
