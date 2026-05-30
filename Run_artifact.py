from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_C_angle(angle=angle, speed_percentage=20)


# Line nine
def Run_Alice(td, ta):
    print("start run")

    # Run starts here
    td.set_speed_percentage(1000000)
    td.straight_drive(-785)  # drive backwards into wall stallll
    td.straight_drive(25)  # drive a little out of wall
    td.turn(-107)
    wait(2)
    td.set_speed_percentage(40)
    td.straight_drive(165)  # drive into mineshaft
    wait(2)
    run_task(ta.move_D_angle(-155, speed_percentage=20))  # pick up cart
    run_task(ta.move_C_angle(-157, speed_percentage=10))  # artifact
    td.straight_drive(-150)  # drive back out
    td.set_speed_percentage(turn_rate_percentage=13)
    td.turn(107)  # slow turn
    td.set_speed_percentage(1000)
    td.straight_drive(850)  # really fast drive back home


# Run ends here

if __name__ == "__main__":
    print()
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_Alice(td, ta)
