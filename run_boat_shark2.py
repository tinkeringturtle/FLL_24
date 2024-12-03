# Author: Meghana, Emma (awesome Team)
#
from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=20)


def run_boat_shark2(td, ta):
    # boat/shark
    # shark
    td.set_speed_percentage(50, 45)
    td.curve(1100, -37)
    td.straight_drive(-150)
    # crab
    td.turn(38)
    td.straight_drive(420)
    run_task(runAttachemnt(ta, 110))
    td.straight_drive(-175)
    run_task(runAttachemnt(ta, -4))
    td.straight_drive(-45)
    run_task(runAttachemnt(ta, -106))
    # boat
    td.turn(-55)
    td.straight_drive(-150)
    # going to other side
    td.straight_drive(150)
    td.set_speed_percentage(15, 10)
    td.turn(30)
    td.set_speed_percentage(25, 10)
    td.straight_drive(100)
    td.set_speed_percentage(50, 50)
    td.straight_drive(100)
    td.turn(25)
    td.set_speed_percentage(70, 70)
    td.straight_drive(500)
    td.turn(35)
    td.straight_drive(670)


"""

    # td.set_speed_percentage(30, 30)
    td.straight_drive(100)
    td.set_speed_percentage(15, 10)
    td.curve(10, 90)
    # td.set_speed_percentage(, 40)
    td.straight_drive(860)
    td.turn(22)
    td.set_speed_percentage(75, 75)
    td.straight_drive(555)

"""
# run has ended


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_boat_shark2(td, ta)
