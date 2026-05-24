import blank
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon, Port, Color
from pybricks.pupdevices import ColorSensor
from pybricks.tools import wait

from TurtleDrive import *
from TurtleAttachement import *

import Run_Cross_The_Terrain, Run_artifact, Run_Bolders
import Run_Map_Reveal, Run_Market, Run_Forum_Plus_Flags, Run_Shipreck
import Run_silo
import A_Toast_To_Treasure, hihi
import Dance_Party

# ================== SENSOR INITIALIZATION ==================
hub = PrimeHub()
bottom_sensor = ColorSensor(Port.E)
front_sensor = ColorSensor(Port.F)


# ================== HSV THRESHOLDS ==================
BLACK_SAT_MAX, BLACK_VAL_MAX = 20, 15
WHITE_SAT_MAX, WHITE_VAL_MIN = 25, 16

RED_SAT_MIN, RED_VAL_MIN = 60, 40
ORANGE_SAT_MIN, ORANGE_VAL_MIN = 70, 60
YELLOW_SAT_MIN, YELLOW_VAL_MIN = 50, 50
LIGHT_GREEN_SAT_MIN, LIGHT_GREEN_VAL_MIN = 30, 40
GREEN_SAT_MIN, GREEN_VAL_MIN = 40, 20
BLUE_SAT_MIN, BLUE_VAL_MIN = 50, 20


# ================== COLOR DETECTION ==================
def get_detected_color(color_data):
    h, s, v = color_data.h, color_data.s, color_data.v

    # BLACK
    if v <= BLACK_VAL_MAX and s <= BLACK_SAT_MAX:
        return "BLACK"

    # WHITE
    if v >= WHITE_VAL_MIN and s <= WHITE_SAT_MAX:
        return "WHITE"

    # ================== FIXED PINK / RED SPLIT ==================

    # PINK = only very dark red (your mat)
    if (h >= 330 or h <= 10) and s >= 70 and v <= 45:
        return "PINK"

    # RED = normal red (everything brighter than pink)
    if (h >= 330 or h <= 10) and s >= 60 and v > 45:
        return "RED"

    # ORANGE
    if 6 <= h <= 45 and s >= ORANGE_SAT_MIN and v >= ORANGE_VAL_MIN:
        return "ORANGE"

    # YELLOW
    if 46 <= h <= 80 and s >= YELLOW_SAT_MIN and v >= YELLOW_VAL_MIN:
        return "YELLOW"

    # LIGHT GREEN
    if 85 <= h <= 110 and s >= LIGHT_GREEN_SAT_MIN and v >= LIGHT_GREEN_VAL_MIN:
        return "LIGHT_GREEN"

    # GREEN
    if 110 <= h <= 170 and s >= GREEN_SAT_MIN and v >= GREEN_VAL_MIN:
        return "GREEN"

    # BLUE
    if 190 <= h <= 270 and s >= BLUE_SAT_MIN and v >= BLUE_VAL_MIN:
        return "BLUE"

    return "UNKNOWN"


# ================== DRIVE SETUP ==================
td = TurtleDrive()
ta = TurtleAttachment()


# ================== START BUTTON ==================
hub.light.on(Color.BLUE)
while not any(hub.buttons.pressed()):
    wait(10)
hub.light.off()


# ================== MAIN LOOP ==================
while True:
    detected_color = get_detected_color(front_sensor.hsv())
    buttons = hub.buttons.pressed()

    if detected_color == "RED":
        hub.light.on(Color.RED)
        if Button.RIGHT in buttons:
            td.stop()
            A_Toast_To_Treasure.run_Elly(td, ta)
            while Button.RIGHT in hub.buttons.pressed():
                wait(10)

    elif detected_color == "PINK":
        hub.light.on(Color.RED)
        if Button.RIGHT in buttons:
            td.stop()
            Run_Forum_Plus_Flags.Run_Forum_Plus_Flags(td, ta)
            while Button.RIGHT in hub.buttons.pressed():
                wait(10)

    elif detected_color == "ORANGE":
        hub.light.on(Color.ORANGE)
        if Button.RIGHT in buttons:
            td.stop()
            Run_Forum_Plus_Flags.Run_Forum_Plus_Flags(td, ta)
            while Button.RIGHT in hub.buttons.pressed():
                wait(10)

        if Button.LEFT in buttons:
            td.stop()
            Dance_Party.run_2nd_Flag(td, ta)
            while Button.LEFT in hub.buttons.pressed():
                wait(10)

    elif detected_color == "YELLOW":
        hub.light.on(Color.YELLOW)
        if Button.RIGHT in buttons:
            td.stop()
            Run_Bolders.run_bolders(td, ta)
            while Button.RIGHT in hub.buttons.pressed():
                wait(10)

    elif detected_color == "WHITE":
        hub.light.on(Color.WHITE)
        if Button.LEFT in buttons:
            td.stop()
            Run_Market.run_market(td, ta)
            while Button.LEFT in hub.buttons.pressed():
                wait(10)

    elif detected_color == "GREEN":
        hub.light.on(Color.GREEN)
        if Button.RIGHT in buttons:
            td.stop()
            Run_Map_Reveal.run_Map_Reveal(td, ta)
            while Button.RIGHT in hub.buttons.pressed():
                wait(10)

    elif detected_color == "LIGHT_GREEN":
        hub.light.on(Color.GREEN)
        if Button.RIGHT in buttons:
            td.stop()
            Run_Shipreck.run_Shipreck(td, ta)
            while Button.RIGHT in hub.buttons.pressed():
                wait(10)

    elif detected_color == "BLUE":
        hub.light.on(Color.BLUE)
        if Button.RIGHT in buttons:
            td.stop()
            hihi.Run_blank(td, ta)
            while Button.RIGHT in hub.buttons.pressed():
                wait(10)

    elif detected_color == "BLACK":
        hub.light.off()
        Run_artifact.Run_Alice(td, ta)

    else:
        hub.light.off()

    wait(50)
