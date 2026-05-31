from TurtleDrive import *
from TurtleAttachement import *

# from pybricks.tools import wait, multitask, run_task


# line nine
def Run_going(td, ta):

    td.straight_drive(795)  # getting out of home area (black)
    td.turn(90)  # turn towards the balls
    td.straight_drive(430)  # drive towards ramp
    td.turn(93)  # turn in front of ramp
    ##guesing from here
    td.straight_drive(300)  # going up the ramp
    td.turn(-90)  # turning into blue
    td.straight_drive(170)  # all the way through


# run begins here


# Main Function
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_going(td, ta)
