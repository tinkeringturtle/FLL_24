# Anshi, Alice

from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_C_angle(angle=angle, speed_percentage=50)


def run_whale(td, ta):
    td.set_speed_percentage(speed_percentage=60)
    td.straight_drive(685)
    td.turn(45)
    td.set_speed_percentage(speed_percentage=10)
    td.straight_drive(185)
    run_task(runAttachemnt(ta, -90))
    td.stop()
    td.set_speed_percentage(speed_percentage=60)
    td.straight_drive(-160)
    td.set_speed_percentage(speed_percentage=10)
    td.turn(132)
    td.set_speed_percentage(speed_percentage=39)
    td.straight_drive(-278)
    td.set_speed_percentage(speed_percentage=60)
    td.straight_drive(900)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_whale(td, ta)
