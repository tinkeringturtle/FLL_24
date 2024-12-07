# Author: Meghana, Emma (awesome Team )
#
from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=20)


def run_boat_shark2(td, ta):
    # boat/shark

    td.set_speed_percentage(50, 45)
    td.curve(1090, -40)
    td.straight_drive(-150)
    td.turn(46)
    # crab
    td.straight_drive(420)
    run_task(runAttachemnt(ta, 110))
    td.straight_drive(-220)
    run_task(runAttachemnt(ta, -1))
    td.straight_drive(-50)
    run_task(runAttachemnt(ta, -110))
    # boat
    td.turn(-55)
    td.straight_drive(-175)
    # going to other side
    td.straight_drive(130)
    td.set_speed_percentage(15, 10)
    td.turn(17)
    td.set_speed_percentage(25, 10)
    td.straight_drive(60)
    td.set_speed_percentage(50, 50)
    td.straight_drive(100)
    td.turn(25)
    td.set_speed_percentage(70, 70)
    td.straight_drive(485)
    td.turn(45)
    td.straight_drive(1200)


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
