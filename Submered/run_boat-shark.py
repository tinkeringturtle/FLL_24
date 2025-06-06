# Author: Meghana, Emma (SIGMAMAMAM (im talking about megna) )
#boat and coral run
#
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=20)


def run_boat_shark(td, ta):
    td.set_speed_percentage(30)
    td.straight_drive(200)#delivering coral
    run_task(runAttachemnt(ta, 80))#picking up boat
    td.straight_drive(-200)#bringing boat home


# run ends here

if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_boat_shark(td, ta)
