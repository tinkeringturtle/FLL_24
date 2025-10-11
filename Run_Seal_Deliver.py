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


# this is the code for the attachment: run_task(ta.move_D_angle(90))


# line nine
def Run_Seal_Deliver(td, ta):
    print("start run")
    # run starts here
    td.straight_drive(200)
    td.turn(35)
    td.set_speed_percentage(30)
    td.straight_drive(275)
    td.set_speed_percentage(20)
    td.straight_drive(-50)
    td.set_speed_percentage(100)
    td.straight_drive(-350)


# run starts here
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_Seal_Deliver(td, ta)
