from TurtleDrive import *
from TurtleAttachement import *


async def runAttachment(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=(100))


def run_Elly(td, ta):

    print("start run")
    td.straight_drive(570)

    async def runAttachment(ta, angle):
        await ta.move_D_angle(angle=angle, speed_percentage=(100))

    run_task(ta.move_D_angle(-555))  # spins Angler Artifact)
    td.straight_drive(-100)


# MAIN FUNCTION
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Elly(td, ta)


# this is the old codeeeeee
"""td.straight_drive(480)

    async def runAttachment(ta, angle):
        await ta.move_D_angle(angle=angle, speed_percentage=(100))

    run_task(ta.move_D_angle(555))  # spins Angler Artifact)
    td.straight_drive(-480)
"""
