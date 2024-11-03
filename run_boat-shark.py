# Author: Meghana, Emma (awesome Team)
#
from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=10)


def run_boat_shark():
    td = TurtleDrive()
    ta = TurtleAttachment()
    # run starts from here

    # coral
    td.set_speed_percentage(20, 25)
    td.straight_drive(162)
    td.straight_drive(-162)
    wait(5000)
    # delivering shark (and(trident?)
    td.set_speed_percentage(50, 50)
    td.straight_drive(720)
    td.straight_drive(-80)
    td.turn
    td.straight_drive(50)
    ta.move_C_angle(-60)
    # getting boat
    td.turn(-45)
    td.straight_drive(-200)
    td.straight_drive(160)
    td.set_speed_percentage(15, 10)
    td.turn(75)
    td.set_speed_percentage(70, 40)
    td.straight_drive(860)
    td.turn(25)
    td.straight_drive(550)
    # run has ended


if __name__ == "__main__":
    run_boat_shark()
