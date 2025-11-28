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


# curve turn - first number is radius, second number is angle.
# this is the code for the attachment: run_task(ta.move_D_angle(90))
# code for looping motor: for i in range(10)
#   run_task(ta.move_D_angle(-300))


# line eight (second black line)
def Run_Seal_Deliver(td, ta):
    print("start run")
    # second balck line from the left, (on the right edge)
    # run starts here
    td.straight_drive(550)  # forward
    td.set_speed_percentage(turn_rate_percentage=30)
    td.curve(215, 155)  # curving in
    td.straight_drive(30)  # going in to raise arm
    run_task(ta.move_D_angle(-100))  # lifting arm
    td.set_speed_percentage(25)
    td.straight_drive(60)  # going in for artifacts
    td.set_speed_percentage(50)
    td.straight_drive(-150)  # backing up
    td.turn(-50)
    td.straight_drive(-120)
    td.curve(-100, 75)
    td.set_speed_percentage(100)
    td.straight_drive(-700)


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
