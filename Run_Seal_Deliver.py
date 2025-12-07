from TurtleDrive import *
from TurtleAttachement import *


def set_speed_percentage(
    self,
    speed_percentage=DEFAULT_SPEED_PERCENTAGE,
    acceleration_percentage=DEFAULT_ACCELERATION_PERCENTAGE,
    turn_rate_percentage=DEFAULT_TURN_RATE_PERCENTAGE,
    turn_acceleration_percentage=DEFAULT_TURN_ACCELERATION_PERCENTAGE,
):

    async def runAttachemnt(ta, angle):
        await ta.move_D_angle(angle=angle, speed_percentage=(5))


# curve turn - first number is radius, second number is angle.
# this is the code for the attachment: run_task(ta.move_D_angle(90))
# code for looping motor: for i in range(10)
#   run_task(ta.move_D_angle(-300))


# line 6. 1 and half (black lines)
def Run_Seal_Deliver(td, ta):
    print("start run")

    # async def runAttachemnt(ta, angle):
    # await ta.move_C_angle(angle=angle, speed_percentage=(5))

    # second balck line from the left, (on the right edge)
    # run starts here
    td.straight_drive(260)
    td.curve(6, 53)
    td.straight_drive(260)
    td.straight_drive(-260)
    td.curve(6, -55)
    td.straight_drive(345)
    td.curve(170, 145)  # curving in
    run_task(ta.move_D_angle(220))  # dropping arm
    td.set_speed_percentage(20)
    td.straight_drive(155)  # driving in

    async def runAttachemnt(ta, angle):
        await ta.move_D_angle(angle=(-100), speed_percentage=(5))

    run_task(ta.move_D_angle(-65))  # lifting arm #45 if not working after run 1.
    wait(5)
    td.turn(-15)
    wait(5)
    td.turn(10)
    td.set_speed_percentage(50)
    # td.set_speed_percentage(turn_rate_percentage=30)
    # td.turn(-11)  # turn before backing out
    td.straight_drive(-30)
    # td.turn(-15)
    # td.straight_drive(-138)
    # td.turn(80)
    # td.set_speed_percentage(670)
    # td.straight_drive(770)


# run ends here
if __name__ == "__main__":
    print()
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_Seal_Deliver(td, ta)


# old code :

# td.curve(90, 75)
# td.set_speed_percentage(40)  # slowing down
# td.straight_drive(270)  # going into the area
# run_task(ta.move_D_angle(500))  # lowering arm
# td.straight_drive(100)
# run_task(ta.move_D_angle(-500))  # lifting arm
# td.set_speed_percentage(20)
# td.straight_drive(-50)  # drive back a little bit slowly
# td.set_speed_percentage(100)  # speed up
# td.straight_drive(-350)  # drive back at full speed


# td.turn(57)
# td.straight_drive(325)
