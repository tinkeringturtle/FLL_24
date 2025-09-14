from TurtleDrive import *
from TurtleAttachement import *

#11th line from right
# line nine
def run_Anshi(td, ta):
    print("start run")
    td.straight_drive(-100)
    td.curve(-175, 115, wait=True)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Anshi(td, ta)
