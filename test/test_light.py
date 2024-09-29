from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait

hub = PrimeHub()

# Blick RED light 10 times, only for testing
for i in range(10):
    hub.light.on(Color.RED)
    wait(1000)
    hub.light.off()
    wait(500)