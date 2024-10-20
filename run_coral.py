# Author: Nitya, Page

from TurtleDrive import *
from TurtleAttachement import *


async def move_down(ta):
    await multitask(
        ta.move_C_angle(angle=120, speed_percentage=5),
        ta.move_D_angle(angle=-20, speed_percentage=5),
    )


async def move_down2(ta):
    await ta.move_D_angle(angle=-15, speed_percentage=3)
    await ta.move_C_angle(angle=110, speed_percentage=8)
    # ta.run_D_until_stalled()
    # await ta.move_C_angle(angle=-110, speed_percentage=5)
    # ta.move_C_time(2000, )


async def runAttachemnt(ta, angle, speed):
    await ta.move_D_angle(angle=angle, speed_percentage=speed)


def runCoral(td, ta):
    td.set_speed_percentage(50)
    ta.move_D_time(speed_percentage=20, time_millisec=200)
    td.straight_drive(665)
    ta.move_D_time(speed_percentage=20, time_millisec=200)
    run_task(runAttachemnt(ta, -60, 15))  # lowering arm for jimmy
    td.set_speed_percentage(30)
    td.turn(-85)
    td.set_speed_percentage(50)
    td.straight_drive(60)
    run_task(runAttachemnt(ta, 20, 8))  # raising jimmy
    wait(400)
    # ta.move_D_angle_sync(30,8)
    td.straight_drive(-10)
    td.turn(90)
    td.straight_drive(40)  #
    td.turn(-50)
    td.set_speed_percentage(40)
    td.straight_drive(120)  # driving into shark
    td.straight_drive(-150)
    td.set_speed_percentage(30)
    td.turn(140)
    td.straight_drive(160)
    td.turn(-95)
    td.set_speed_percentage(14)
    td.straight_drive(50)
    ta.move_C_time(speed_percentage=20, time_millisec=200)
    run_task(move_down2(ta))

    ta.move_C_angle_sync(-50)
    td.set_speed_percentage(75)
    td.straight_drive(-400)
    td.turn(60)
    td.straight_drive(-200)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    runCoral(td, ta)
    # run_task(move_down(ta))
