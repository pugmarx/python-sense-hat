#!/usr/bin/python
import sys
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
red = (255, 0, 0)
white = (255, 255, 255)
other = (10, 25, 25)
green = (0, 255, 0)
#sense.show_message("One small step for Pi!", text_colour=red)
#sense.clear(255, 255, 255)
sense.low_light = True
sense.show_message(str(sys.argv[1]), text_colour=other)
