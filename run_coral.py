# Author: Nitya, Page

from TurtleDrive import *
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
    td.set_speed_percentage(50)
    ta.move_D_time(speed_percentage=20, time_millisec=200)  # reseting arm
    td.straight_drive(635)  # driving to coral
    ta.move_D_time(speed_percentage=20, time_millisec=200)
    run_task(runAttachemnt(ta, 60, 15))  # lowering arm for jimmy
    td.set_speed_percentage(30)
    td.turn(-85)  # To drive into coral to get jimmy
    td.set_speed_percentage(50)
    td.straight_drive(70)  # driving into mission model
    run_task(runAttachemnt(ta, -100, 10))  # raising jimmy
    wait(400)
    td.straight_drive(-45)  # driving back from the coral mission
    # starting shark
    td.turn(85)  # turn to face shark
    td.straight_drive(80)  # driving closer to shark
    td.turn(-50)  # to get ready to turn into shark
    td.set_speed_percentage(40)
    td.straight_drive(200)  # drives into shark
    td.straight_drive(-5)  # driving away from shark
    td.turn(-10)
    td.set_speed_percentage(30)
    ta.move_C_angle()
    # ta.move_C_time(speed_percentage=100, time_millisec=2000)
    run_task(runAttachemntC(ta, -500, 100))
    run_task(runAttachemntC(ta, 500, 100))
    td.straight_drive(-100)
    td.turn(70)
    td.set_speed_percentage(130)
    td.straight_drive(-745)


# lifting D arm so for


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    runCoral(td, ta)
    # run_task(move_down(ta))
