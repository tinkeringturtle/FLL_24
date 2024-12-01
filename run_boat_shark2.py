# Author: Meghana, Emma (awesome Team)
#
from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=20)


def run_boat_shark2(td, ta):
    # boat/shark
    # shark
    td.set_speed_percentage(50, 50)
    td.straight_drive(710)
    td.straight_drive(-150)
    # crab
    td.turn(27)
    td.straight_drive(400)
    run_task(runAttachemnt(ta, 110))
    td.straight_drive(-175)
    run_task(runAttachemnt(ta, -5))
    td.straight_drive(-37)
    run_task(runAttachemnt(ta, -105))
    # boat
    td.turn(-55)
    td.straight_drive(-140)
    td.straight_drive(150)
    td.set_speed_percentage(15, 10)
    td.turn(30)
    td.set_speed_percentage(25, 10)
    td.straight_drive(100)
    td.set_speed_percentage(50, 50)
    td.straight_drive(100)
    td.turn(20)
    td.set_speed_percentage(70, 70)
    td.straight_drive(500)
    td.turn(37)
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
