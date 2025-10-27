from TurtleDrive import *
from TurtleAttachement import *
from pybricks.tools import wait, multitask, run_task




def run_market(td, ta):
    td.straight_drive(220)

    td.turn(-50)
    td.straight_drive(280)
    run_task(ta.move_C_angle(200))
    
    td.straight_drive(40)
    td.straight_drive(-190)
    
    td.straight_drive(120)
    run_task(ta.move_C_angle(-200))
    td.straight_drive(-300)

    td.straight_drive(420) 
    ta.move_D_time(speed_percentage=-100, time_millisec=800)
    ta.move_D_time(speed_percentage=100, time_millisec=1000)
    ta.move_D_time(speed_percentage=-100, time_millisec=800)
    ta.move_D_time(speed_percentage=100, time_millisec=1000)
    ta.move_D_time(speed_percentage=-100, time_millisec=800)
    ta.move_D_time(speed_percentage=100, time_millisec=1000)
    ta.move_D_time(speed_percentage=-100, time_millisec=800)
    ta.move_D_time(speed_percentage=100, time_millisec=1500)

  
   


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_market(td, ta)

