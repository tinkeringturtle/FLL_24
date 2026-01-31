from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from TurtleDrive import *
from TurtleAttachement import *

# Initialize sensor
sensor = ColorSensor(Port.E)


def detect_bottom_color(td):
    # 1. Measure the 'White' floor before moving
    starting_brightness = sensor.hsv().v
    # Define black as 30% darker than the start
    threshold = starting_brightness * 0.7

    print("Starting Brightness:", starting_brightness)
    print("Target Threshold:", threshold)

    # 2. Start moving forward
    td.turn_drive(100, 0, 0)

    while True:
        current_v = sensor.hsv().v

        if current_v < threshold:
            td.stop()
            print("Detected Black!")
            break

        wait(10)


def run_Anshi(td, ta):
    # Mission Steps
    td.straight_drive(-250)
    td.straight_drive(1060)

    # Line Detection
    detect_bottom_color(td)

    # Full stop before turn
    td.stop()
    wait(500)

    # Final Turn
    td.set_speed_percentage(50)
    td.turn(41)
    run_task(ta.move_D_angle(-500))
    td.straight_drive(190)
    td.turn(10.9)
    td.straight_drive(100)
    td.straight_drive(-235)
    td.set_speed_percentage(100)
    run_task(ta.move_D_angle(230))
    td.turn(-60)
    td.straight_drive(1000)
    return
    td.turn(-50)
    td.straight_drive(500)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Anshi(td, ta)

# --- Main Execution ---
# td = TurtleDrive()
# ta = TurtleAttachment()

# Call the function ONLY ONCE so it doesn't restart and move back
# run_Anshi(td, ta)
