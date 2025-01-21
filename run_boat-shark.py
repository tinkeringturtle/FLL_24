# Author: Meghana, Emma (awesome Team )
#
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=20)


def run_boat_shark(td, ta):
    td.set_speed_percentage(30)
    td.straight_drive(200)
    run_task(runAttachemnt(ta, 80))
    td.straight_drive(-200)


# run ends here

if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_boat_shark(td, ta)
