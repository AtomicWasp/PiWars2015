#!/usr/bin/python

# leds.py (NeoPixel LED Driver) by George P Tuli of Positronic for Pi Wars 2015.

# Import the required libraries.
import unicornhat as UH
import time
import random

# Set the LED brightness for all pixels.
UH.brightness(1.0)

# Define the lenth of the LED array.
strip_length = 8

# Continuously...
while True:
	# Generate random values of RGB, within a suitable range.
	red = random.randint(80, 256)
	green = random.randint(80, 256)
	blue = random.randint(80, 256)
	
	# Turn on the LEDs, in a pattern.
	for led in range(strip_length):
		UH.set_pixel(0, led, int(red), int(green), int(blue))
		UH.show()
		UH.set_pixel(0, led, 0, 0, 0)
		time.sleep(0.05)
