# Task 2:

from microbit import *
import radio

radio.on()

while True:
    # Searches for a message, and scrolls it once it has been received
    message = radio.receive()
    if message is not None: # Displays message if one has been received
        display.scroll(message)