# Import Libaries
from assets.arduino import *
from assets.library import *
from assets.interface.PhoneCall import *
from assets.interface.WebBrowsing import *

# Checking which function the switch is on
while True:
    if switch.on():
        # Detect Input

        # Run Internet browsing function
        WebBrowsing()

        # OutPut
    else:
        # Detect Input

        # Connect to phone call
        PhoneCall()