# Anshi, Alice
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from TurtleDrive import *
from TurtleAttachement import *

# 10th line attachment


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=80)


def run_submersible(td, ta):
    td.set_speed_percentage(65, 60)
    td.straight_drive(500)
    td.turn(-50)
    td.set_speed_percentage(80, 75)
    td.straight_drive(650)
    td.set_speed_percentage(55, 50)
    td.turn(20)
    td.straight_drive(-280)  # -300 hitting model
    td.turn(-16)
    td.straight_drive(235)
    run_task(runAttachemnt(ta, -450))
    # wait(1050)
    td.straight_drive(-220)  # -240 hitting model again
    td.turn(-45)
    td.straight_drive(430)
    td.straight_drive(-200)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_submersible(td, ta)
