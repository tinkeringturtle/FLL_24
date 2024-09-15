from TurtleDrive import *


def run():
    td = TurtleDrive()
    print(td.get_speed())
    # to drive stright do - td.drive(x mm)
    td.set_speed(turn_rate=100, turn_acceleration=350)  # for sunset
    td.drive(100)
    td.turn(90)


run()
