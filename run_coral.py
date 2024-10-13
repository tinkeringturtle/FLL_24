# Author: Nitya, Page

from TurtleDrive import *
from TurtleAttachement import *


async def move_down(ta):
    await multitask(
        ta.move_C_angle(angle=120, speed_percentage=10),
        ta.move_D_angle(angle=-35, speed_percentage=10),
    )


async def runAttachemnt(ta, angle, speed):
    await ta.move_D_angle(angle=angle, speed_percentage=speed)


def runCoral(td, ta):
    td.set_speed_percentage(50)
    ta.move_D_time(speed_percentage=20, time_millisec=200)
    td.straight_drive(665)
    ta.move_D_time(speed_percentage=20, time_millisec=200)
    run_task(runAttachemnt(ta, -50, 15))  # lowering arm for jimmy
    td.set_speed_percentage(30)
    td.turn(-85)
    td.set_speed_percentage(50)
    td.straight_drive(60)
    run_task(runAttachemnt(ta, 20, 10))  # raising jimmy
    td.straight_drive(-10)
    td.turn(90)
    td.straight_drive(40)
    td.turn(-50)
    td.set_speed_percentage(40)
    td.straight_drive(120)
    td.straight_drive(-150)
    td.set_speed_percentage(30)
    td.turn(140)
    td.straight_drive(160)
    td.turn(-95)
    td.straight_drive(45)
    run_task(move_down(ta))


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    runCoral(td, ta)
    # run_task(move_down(ta))
