# Author: Nitya, Page

from TurtleDrive.py import *
from TurtleAttachement import *


async def move_down(ta):
    await multitask(
        ta.move_C_angle(angle=120, speed_percentage=5),
        ta.move_D_angle(angle=-20, speed_percentage=5),
    )


async def move_down2(ta):
    await ta.move_D_angle(angle=-13, speed_percentage=3)
    await ta.move_C_angle(angle=110, speed_percentage=6.5)
    # ta.run_D_until_stalled()
    # await ta.move_C_angle(angle=-110, speed_percentage=5)
    # ta.move_C_time(2000, )


async def runAttachemnt(ta, angle, speed):
    await ta.move_D_angle(angle=angle, speed_percentage=speed)


async def runAttachemntC(ta, angle, speed):
    await ta.move_C_angle(angle=angle, speed_percentage=speed)


def runCoral(td, ta):
    td.set_speed_percentage(80, 75)
    # ta.move_D_time(speed_percentage=20, time_millisec=200)  # reseting arm
    td.straight_drive(70)  # driving to coral
    td.turn(45)  # turning
    td.straight_drive(270)
    td.turn(-45)
    td.straight_drive(405)
    ta.move_D_time(speed_percentage=20, time_millisec=200)
    run_task(runAttachemnt(ta, 100, 15))  # lowering arm for jimmy
    # wait(100)
    td.set_speed_percentage(50, 45)
    td.turn(-88)  # To drive into coral to get jimmy
    # td.set_speed_percentage(30, 25)
    run_task(ta.run_C_until_stalled(-90))  # lower arm for tree
    # run_task(
    #   ta.move_C_angle(-470, then=Stop., wait=True)
    # )  # lowering arm for coral tree
    td.set_speed_percentage(80, 75)
    td.straight_drive(125)  # about to drive into mission model

    run_task(ta.run_C_until_stalled(80))  # raise tree
    # run_task(
    #    ta.move_C_angle(515, then=Stop.COAST_SMART, wait=False)
    # )  # raising the coral tree
    run_task(runAttachemnt(ta, -125, 100))  # raising jimmy
    td.straight_drive(-70)  # driving back from the coral mission
    td.turn(50)
    td.straight_drive(220)
    td.set_speed_percentage(100, 95)
    td.straight_drive(-260)  # backing away from shark
    td.turn(55)
    td.straight_drive(-655)  # driving home


# lifting D arm so for


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    runCoral(td, ta)
    # run_task(move_down(ta))
