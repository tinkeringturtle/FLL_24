# Author: Meghana, Emma (awesome Team)
#
from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=100)


def run_boat_shark(td, ta):

    # run starts from here
    # coral
    td.set_speed_percentage(20)
    td.straight_drive(200)
    # run_task(runAttachemnt(ta, 100))
    td.set_speed_percentage(60)
    td.straight_drive(-400)


# run has ended


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_boat_shark(td, ta)
