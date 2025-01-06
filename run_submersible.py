# Anshi, Alice
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from TurtleDrive import *
from TurtleAttachement import *

# 10th line attachment


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=50)


def run_submersible(td, ta):
    td.set_speed_percentage(speed_percentage=60)
    td.straight_drive(500)
    td.turn(-47)
    td.set_speed_percentage(80)
    td.straight_drive(650)
    td.set_speed_percentage(50)
    td.turn(20)
    td.straight_drive(-300)
    td.turn(-16)
    td.straight_drive(225)
    run_task(runAttachemnt(ta, -450))
    wait(1050)
    td.straight_drive(-230)
    td.turn(-50)
    td.straight_drive(410)
    td.straight_drive(-200)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_submersible(td, ta)
