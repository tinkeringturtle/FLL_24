# Anshi, Alice
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=50)


def run_submersible(td, ta):
    td.set_speed_percentage(speed_percentage=60)
    td.straight_drive(500)
    # <<<<<<< HEAD
    td.turn(-47)
    td.straight_drive(200)
    # td.turn(-85)
    td.straight_drive(400)
    td.set_speed_percentage(speed_percentage=40)
    td.straight_drive(-100)
    td.turn(-35)
    td.straight_drive(70)
    td.turn(35)
    # td.turn(50)
    # td.straight_drive(80)
    # td.turn(30)
    # td.straight_drive(80)
    # td.turn(-90)
    # td.straight_drive(30)
    # td.turn(90)
    # td.straight_drive(-150)
    # td.turn(-35)
    # td.straight_drive(157)
    # run_task(runAttachemnt(ta, -450))
    # wait(1000)
    # td.straight_drive(-60)=
    td.turn(-50)
    td.straight_drive(650)
    td.straight_drive(-150)
    td.turn(-35)
    td.straight_drive(70)
    td.turn(20)
    td.straight_drive(80)
    run_task(runAttachemnt(ta, -450))
    wait(1050)
    td.straight_drive(-80)
    td.turn(65)
    td.straight_drive(-60)
    # td.turn(30)
    # td.straight_drive(80)
    # td.turn(-90)
    # td.straight_drive(30)
    # td.turn(90)
    # td.straight_drive(-150)
    # td.turn(-35)
    # td.straight_drive(157)
    # run_task(runAttachemnt(ta,-450))
    # wait(1000)
    # td.straight_drive(-60)


# >>>>>>> cc63350 (working on master code)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_submersible(td, ta)
