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


def runCoral(td, ta):
    td.set_speed_percentage(50)
    ta.move_D_time(speed_percentage=20, time_millisec=200)  # reseting arm
    td.straight_drive(665)  # driving to coral
    ta.move_D_time(speed_percentage=20, time_millisec=200)
    run_task(runAttachemnt(ta, -60, 15))  # lowering arm for jimmy
    td.set_speed_percentage(30)
    td.turn(-85)  # To drive into coral to get jimmy
    td.set_speed_percentage(50)
    td.straight_drive(65)  # driving into mission model
    run_task(runAttachemnt(ta, 20, 10))  # raising jimmy
    wait(400)
    td.straight_drive(-15)  # driving back from the coral mission
    # starting shark
    td.turn(90)  # turn to face shark
    td.straight_drive(40)  # driving closer to shark
    td.turn(-50)  # to get ready to turn into shark
    td.set_speed_percentage(40)
    td.straight_drive(120)  # drives into shark
    td.straight_drive(-155)  # driving away from shark
    td.set_speed_percentage(30)
    # starting nursery
    td.turn(140)  # turn to go closer to nursery
    td.straight_drive(160)  # to be in front of nursery, not face in front
    td.turn(-95)  # turn with face in front of nursery
    td.set_speed_percentage(14)
    td.straight_drive(50)  # to drive into nursery
    run_task(runAttachemnt(ta, -35, 15))
    ta.move_C_time(speed_percentage=20, time_millisec=500)  # to lower  arms
    run_task(runAttachemnt(ta, 40, 15))  # bringing C arm up
    td.set_speed_percentage(75)
    td.straight_drive(-400)  # backing from mission model
    td.turn(60)  # turning to get home
    td.straight_drive(-475)  # WE GOING HOME
    run_task(
        runAttachemnt(ta, 80, 15)
    )  # lifting D arm so for 2nd run we won't have to do it


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    runCoral(td, ta)
    # run_task(move_down(ta))
