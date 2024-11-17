# Anshi, Alice

from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_C_angle(angle=angle, speed_percentage=30)


# line nine
def run_whale(td, ta):
    td.set_speed_percentage(speed_percentage=60)
    td.straight_drive(685)
    td.turn(43)
    td.set_speed_percentage(speed_percentage=10)
    td.straight_drive(160)
    run_task(runAttachemnt(ta, -50))
    td.stop()
    td.set_speed_percentage(speed_percentage=60)
    td.straight_drive(-165)
    td.set_speed_percentage(speed_percentage=10)
    td.turn(130)
    td.set_speed_percentage(speed_percentage=39)
    td.straight_drive(-265)
    td.set_speed_percentage(speed_percentage=5)
    td.turn(30)
    td.turn(-30)
    td.set_speed_percentage(speed_percentage=60)
    td.straight_drive(550)
    td.curve(500, -54)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_whale(td, ta)
