# Author: Meghana, Emma (awesome Team)
#
from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_C_angle(angle=angle, speed_percentage=100)


def run_boat_shark(td, ta):

    # run starts from here
    # coral
    td.set_speed_percentage(20, 25)
    td.straight_drive(162)
    td.straight_drive(-162)
    td.brake()
    wait(7000)
    # boat/shark
    td.set_speed_percentage(50, 50)
    td.straight_drive(710)
    td.turn(-45)
    td.straight_drive(-200)
    td.set_speed_percentage(30, 50)
    td.straight_drive(160)
    td.set_speed_percentage(15, 10)
    td.turn(75)
    td.set_speed_percentage(70, 40)
    td.straight_drive(860)
    td.turn(22)
    td.set_speed_percentage(100, 100)
    td.straight_drive(555)

    # run has ended


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_boat_shark(td, ta)
