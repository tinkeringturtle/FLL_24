# line up is the right side of the second black line
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
        await ta.move_C_angle(angle=angle, speed_percentage=20)


# line nine
def Run_artifact(td, ta):
    print("start run")

    # Run starts here

    td.set_speed_percentage(100)
    td.straight_drive(-795)#drive backwards into wall
    td.straight_drive(25)#drive a little out of wall
    td.turn(-107)#turn towards the mineshaft
    td.set_speed_percentage(10)
    td.straight_drive(145)#drive into mineshaft
    wait(2)
    set_speed_percentage(1)
    run_task(ta.move_D_angle(-110))#pick up artifact
    run_task(ta.move_C_angle(-135))#lift up cart onto other side
    td.straight_drive(-130)#drive back out
    td.set_speed_percentage(turn_rate_percentage=5)
    td.turn(107)#slow turn
    td.set_speed_percentage(200)
    td.straight_drive(850)#really fast drive back home


# Run ends here

# run_task(ta.move_C_angle(-130))
# td.straight_drive(-100)


# ATTACHEMENT MOVEMENT ANGLES
# run_task(ta.move_D_angle(90))  ----- USE THIS CODE ----------- NEGATIVE = UP.  POSOTIVE = DOWN.
# run_task(runAttachemnt(ta, 180))
# run_task(runAttachemnt(ta, -180))


# COMMENTED CODE:

# td.straight_drive(15)
# td.turn(90)

# td.straight_drive(500)
# td.turn(25)
# td.straight_drive(360)
# td.turn(90)

# run_task(ta.move_C_angle(-130))
# td.straight_drive(-100)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_Seal_Jones(td, ta)
