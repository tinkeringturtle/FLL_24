from TurtleDrive import *

td = TurtleDrive()
# to drive stright do - td.drive(x mm)


print(td.get_speed())
td.drive(200)


td.set_speed(speed=300)
td.drive(200)

print(td.get_speed())

td.turn(-90)
td.drive(200)
td.turn(90)




'''
if __name__ == "__main__":
    
'''