import On_the_spot
import On_the_spot_giong_home
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color
from pybricks.tools import wait

from TurtleDrive import *
from TurtleAttachement import *

# ================== INITIALIZATION ==================
hub = PrimeHub()
td = TurtleDrive()
ta = TurtleAttachment()

# ================== INITIAL START BUTTON ==================
# Robot turns BLUE and waits for any button press to activate the main menu loop
hub.light.on(Color.BLUE)
while not any(hub.buttons.pressed()):
    wait(10)
hub.light.off()
wait(500)  # Short pause so the initial press doesn't instantly trigger a mission


# ================== MAIN LOOP ==================
while True:
    buttons = hub.buttons.pressed()
    # print(buttons)

    # ---- RIGHT BUTTON: ON THE SPOT ----
    if Button.RIGHT in buttons:
        td.stop()
        # hub.light.on(Color.GREEN)  # Optional visual cue that a run started
        print("----------------")
        # Runs the On_the_spot module
        On_the_spot.Run_silo(
            td, ta
        )  # Note: Adjust '.run' if your file uses a different function name

        # Wait until the button is released so it doesn't loop infinitely
        # while Button.RIGHT in hub.buttons.pressed():
        #    wait(10)
        # hub.light.off()

    # ---- LEFT BUTTON: ON THE SPOT GOING HOME ----
    elif Button.LEFT in buttons:
        td.stop()
        print("*******************")
        # hub.light.on(Color.ORANGE)  # Optional visual cue

        # Runs the On_the_spot_giong_home module
        On_the_spot_giong_home.Run_going(
            td, ta
        )  # Note: Adjust '.run' if your file uses a different function name

        # Wait until the button is released
        # while Button.LEFT in hub.buttons.pressed():
        #    wait(10)
        hub.light.off()

    wait(50)
