# Anshi, Alice

from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=50)


def run_submersible(td, ta):
    td.set_speed_percentage(speed_percentage=60)
    td.straight_drive(700)
    td.turn(-85)
    td.straight_drive(400)
    td.set_speed_percentage(speed_percentage=40)
    td.turn(50)
    td.straight_drive(80)
    td.turn(30)
    td.straight_drive(80)
    td.turn(-90)
    td.straight_drive(30)
    td.turn(90)
    td.straight_drive(-150)
    td.turn(-35)
    td.straight_drive(145)
    run_task(runAttachemnt(ta,-450))
    wait(1000)
    td.straight_drive(-60)
    


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_submersible(td, ta)
    