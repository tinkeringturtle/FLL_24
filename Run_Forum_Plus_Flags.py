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


# curve turn - first number is radius, second number is angle(turn).
# this is the code for the attachment: run_task(ta.move_D_angle(90))
# code for looping motor: for i in range(10)
#   run_task(ta.move_D_angle(-300))


# line 6. 1 and half (black lines)
def Run_Forum_Plus_Flags(td, ta):
    print("start run")

    # async def runAttachemnt(ta, angle):
    # await ta.move_C_angle(angle=angle, speed_percentage=(5))

    # new line up = first black line from the right, right side of the robot
    # old line up is 2nd black line from the left
    # run starts here

    td.straight_drive(235)
    td.set_speed_percentage(turn_rate_percentage=7)
    td.turn(44)
    td.straight_drive(260)
    run_task(ta.move_C_angle(-93, speed_percentage=20))  # deliver first flag
    run_task(ta.move_C_angle(200))  # brign arm bakc
    td.straight_drive(-530)
    td.turn(25)
    wait(100)  # ready to leave
    td.set_speed_percentage(1000)
    td.straight_drive(740)
    td.turn(30)
    td.straight_drive(1150.6767)
    # note the rest of the code is for backup incase we need to do 2nd flag + aina. Most likely just make this distnace longer
    # td.curve(500, -48)
    # td.straight_drive(370)
    # td.set_speed_percentage(100)
    # td.straight_drive(-470)
    # td.turn(90)
    # td.straight_drive(820)

    """
    td.set_speed_percentage(30)
    td.straight_drive(252)
    td.curve(6, 53)  # delivering forum curve
    td.set_speed_percentage(40)
    td.straight_drive(300)  # in
    td.straight_drive(-415)  # out
    wait(20)
    td.turn(-30)
    td.set_speed_percentage(70)
    td.straight_drive(505)
    td.set_speed_percentage(95)
    td.straight_drive(-650)
    """
    # td.turn(-10)  # erm like 67?
    # td.curve(6, -55)
    # td.set_speed_percentage(70)
    # td.straight_drive(415)
    # td.turn(80)
    # td.straight_drive(40)
    """
    # td.curve(100, 86)
    ## td.turn(90)
    # td.set_speed_percentage(80)
    # td.straight_drive(260)
    # td.turn(80)
    # our code is gone for now we will only do the forum and one single flag.
    #this is the code for Iana and 3rd flag
    """
    """
    run_task(ta.move_D_angle(495))  # dropping flag
    td.straight_drive(590)
    td.turn(-75)
    td.straight_drive(-35)
    run_task(ta.move_C_angle(-140))  # dropping arm
    td.straight_drive(240)
    """


# run ends here
if __name__ == "__main__":
    print(
        " meghanas italian brainrot comlition: 67 mythical brainrot, tralaleo trala, ballerina cappuchina, tung tung tung sahur, assasino bandito, lirri lirri larilla, los traleritos, trippi troppi, part 2 coming soon!!! )"
    )
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_Forum_Plus_Flags(td, ta)


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


##code for seal:
"""
td.curve(170, 143)  # curving in
    run_task(ta.move_D_angle(220))  # dropping arm
    td.set_speed_percentage(20)
    td.straight_drive(165)  # driving in

    async def runAttachemnt(ta, angle):
        await ta.move_D_angle(angle=(-100), speed_percentage=(5))

    run_task(ta.move_D_angle(-54))  # lifting arm #45 if not working after run 1.
    wait(8)
    td.turn(-20)
    run_task(ta.move_D_angle(-6))
    wait(5)
    td.turn(20)
    td.set_speed_percentage(50)
    td.straight_drive(-130)
    td.turn(-53)
    td.straight_drive(50)
"""
