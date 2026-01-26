from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Port
from pybricks.pupdevices import ColorSensor
from pybricks.tools import wait, run_task
from TurtleDrive import *
from TurtleAttachement import *
import Run_Cross_The_Terrain, Run_artifact, Run_Bolders
import Run_Map_Reveal, Run_Market, Run_Forum_Plus_Flags, Run_Shipreck
import A_Toast_To_Treasure

# --- SENSOR INIT ---
hub = PrimeHub()
bottom_sensor = ColorSensor(Port.E)
front_sensor = ColorSensor(Port.F)

# --- COLOR THRESHOLDS ---
BLACK_SAT_MAX, BLACK_VAL_MAX = 30, 30
WHITE_SAT_MAX, WHITE_VAL_MIN = 40, 80

RED_HUE_MAX1, RED_HUE_MIN2 = 10, 350
RED_SAT_MIN, RED_VAL_MIN = 60, 40

ORANGE_HUE_MIN, ORANGE_HUE_MAX = 11, 45
ORANGE_SAT_MIN, ORANGE_VAL_MIN = 50, 40

YELLOW_HUE_MIN, YELLOW_HUE_MAX = 46, 80
YELLOW_SAT_MIN, YELLOW_VAL_MIN = 50, 50

LIGHT_GREEN_HUE_MIN, LIGHT_GREEN_HUE_MAX = 85, 110
LIGHT_GREEN_SAT_MIN, LIGHT_GREEN_VAL_MIN = 30, 40

GREEN_HUE_MIN, GREEN_HUE_MAX = 110, 170
GREEN_SAT_MIN, GREEN_VAL_MIN = 40, 20

BLUE_HUE_MIN, BLUE_HUE_MAX = 190, 270
BLUE_SAT_MIN, BLUE_VAL_MIN = 50, 20


# --- COLOR DETECTION ---
def get_detected_color(color_data):
    h, s, v = color_data  # unpack tuple

    if v <= BLACK_VAL_MAX and s <= BLACK_SAT_MAX:
        return "BLACK"
    if v >= WHITE_VAL_MIN and s <= WHITE_SAT_MAX:
        return "WHITE"
    if (
        (h <= RED_HUE_MAX1 or h >= RED_HUE_MIN2)
        and s >= RED_SAT_MIN
        and v >= RED_VAL_MIN
    ):
        return "RED"
    if (
        ORANGE_HUE_MIN <= h <= ORANGE_HUE_MAX
        and s >= ORANGE_SAT_MIN
        and v >= ORANGE_VAL_MIN
    ):
        return "ORANGE"
    if (
        YELLOW_HUE_MIN <= h <= YELLOW_HUE_MAX
        and s >= YELLOW_SAT_MIN
        and v >= YELLOW_VAL_MIN
    ):
        return "YELLOW"
    if (
        LIGHT_GREEN_HUE_MIN <= h <= LIGHT_GREEN_HUE_MAX
        and s >= LIGHT_GREEN_SAT_MIN
        and v >= LIGHT_GREEN_VAL_MIN
    ):
        return "LIGHT_GREEN"
    if (
        GREEN_HUE_MIN <= h <= GREEN_HUE_MAX
        and s >= GREEN_SAT_MIN
        and v >= GREEN_VAL_MIN
    ):
        return "GREEN"
    if BLUE_HUE_MIN <= h <= BLUE_HUE_MAX and s >= BLUE_SAT_MIN and v >= BLUE_VAL_MIN:
        return "BLUE"
    return "UNKNOWN"


# --- DRIVE & ATTACHMENT ---
td = TurtleDrive()
ta = TurtleAttachment()

# --- WAIT FOR ANY BUTTON TO START ---
hub.light.on(Color.BLUE)
while not any(hub.buttons.pressed()):
    wait(10)
hub.light.off()

# --- MAIN LOOP ---
while True:
    color_data = front_sensor.hsv()
    detected_color = get_detected_color(color_data)
    buttons = hub.buttons.pressed()

    # DEBUG: see sensor readings
    print("HSV:", color_data, "Detected:", detected_color)

    # RED
    if detected_color == "RED" and Button.RIGHT in buttons:
        hub.light.on(Color.RED)
        td.stop()
        A_Toast_To_Treasure.run_Elly(td, ta)
        while Button.RIGHT in hub.buttons.pressed():
            wait(10)

    # YELLOW
    elif detected_color == "YELLOW" and Button.RIGHT in buttons:
        hub.light.on(Color.YELLOW)
        td.stop()
        Run_Bolders.run_bolders(td, ta)
        while Button.RIGHT in hub.buttons.pressed():
            wait(10)

    # WHITE
    elif detected_color == "WHITE" and Button.LEFT in buttons:
        hub.light.on(Color.YELLOW)
        td.stop()
        Run_Market.run_market(td, ta)
        while Button.LEFT in hub.buttons.pressed():
            wait(10)

    # GREEN
    elif detected_color == "GREEN" and Button.RIGHT in buttons:
        hub.light.on(Color.WHITE)
        td.stop()
        Run_Map_Reveal.run_Map_Reveal(td, ta)
        while Button.RIGHT in hub.buttons.pressed():
            wait(10)

    # LIGHT GREEN
    elif detected_color == "LIGHT_GREEN" and Button.RIGHT in buttons:
        hub.light.on(Color.GREEN)
        td.stop()
        Run_Shipreck.run_Shipreck(td, ta)
        while Button.RIGHT in hub.buttons.pressed():
            wait(10)

    # ORANGE
    elif detected_color == "ORANGE" and Button.RIGHT in buttons:
        hub.light.on(Color.ORANGE)
        td.stop()
        Run_Forum_Plus_Flags.Run_Forum_Plus_Flags(td, ta)
        while Button.RIGHT in hub.buttons.pressed():
            wait(10)

    # BLUE
    elif detected_color == "BLUE" and Button.RIGHT in buttons:
        hub.light.on(Color.BLUE)
        td.stop()
        Run_Cross_The_Terrain.run_Anshi(td, ta)
        while Button.RIGHT in hub.buttons.pressed():
            wait(10)

    # BLACK (auto-start)
    elif detected_color == "BLACK":
        hub.light.off()
        Run_artifact.Run_Alice(td, ta)

    else:
        hub.light.off()

    wait(50)
