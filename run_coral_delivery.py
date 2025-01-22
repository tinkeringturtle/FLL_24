# Author: Meghana, Emma (amazing Team)
#
from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=100)


def run_boat_shark(td, ta):

    # run starts from here
    # coral
    td.set_speed_percentage(20, 15)
    td.straight_drive(200)
    run_task(ta.move_D_angle(80))
    td.set_speed_percentage(65, 60)
    td.straight_drive(-330)


# run has ended


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_boat_shark(td, ta)
