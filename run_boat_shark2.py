# Author: Meghana, Emma (awesome Team)
#
from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_C_angle(angle=angle, speed_percentage=100)


def run_boat_shark2(td, ta):
    # boat/shark
    td.set_speed_percentage(50, 50)
    td.straight_drive(710)
    td.straight_drive(-35)
    td.turn(-100)
    td.set_speed_percentage(25, 25)
    td.straight_drive(-125)
    td.turn(72)
    td.straight_drive(-95) #catching the boat
    td.straight_drive(150)
    td.set_speed_percentage(15, 10)
    td.turn(45)
    td.set_speed_percentage(25, 10)
    td.straight_drive(100)
    td.set_speed_percentage(50, 50)
    td.straight_drive(400)
    td.set_speed_percentage(15, 10)
    td.turn(35)
    td.set_speed_percentage(75, 50)
    td.straight_drive(900)
    # td.set_speed_percentage(10, 10)
    # td.curve(radius=150, angle=55)


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
