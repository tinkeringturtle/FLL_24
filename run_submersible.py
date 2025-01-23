# Anshi, Alice
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from TurtleDrive import *
from TurtleAttachement import *

# 10th line attachment


async def runAttachemnt(ta, angle):
    await ta.move_C_angle(angle=angle, speed_percentage=90)


def run_submersible(td, ta):
    td.set_speed_percentage(65, 60)
    td.straight_drive(460)
    td.turn(-50)
    td.set_speed_percentage(90, 75)
    td.straight_drive(670)
    run_task(runAttachemnt(ta, 430))
    wait(1060)
    td.straight_drive(-225)  # -240 hitting model again
    td.turn(-45)
    td.straight_drive(470)
    td.straight_drive(-200)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_submersible(td, ta)
