from TurtleDrive import *


def run():
    td = TurtleDrive()
    print(td.get_speed_settings())
    # to drive stright do - td.drive(x mm)
    td.set_speed(turn_rate=100, turn_acceleration=350)  # for sunset
    td.straight_drive(500)
    # td.turn(90)
    # td.curve(1000,90)


run()
