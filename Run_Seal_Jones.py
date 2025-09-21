# line up is the right side of the second black line
from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_C_angle(angle=angle, speed_percentage=40)


# line nine
def Run_Seal_Jones(td, ta):
    print("start run")

    # Run starts here

    td.straight_drive(15)
    td.turn(90)


# Run ends here

# run_task(ta.move_C_angle(-130))
# td.straight_drive(-100)


# ATTACHEMENT MOVEMENT ANGLES
# run_task(ta.move_D_angle(90))  ----- USE THIS CODE ----------- NEGATIVE = UP.  POSOTIVE = DOWN.
# run_task(runAttachemnt(ta, 180))
# run_task(runAttachemnt(ta, -180))


# COMMENTED CODE:

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
