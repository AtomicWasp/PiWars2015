#!/usr/bin/python

# ultrasonic.py (The ultrasonic distance sensor library) by George P Tuli of Positronic for Pi Wars 2015.

# Import the required libraries.
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Setup the two pins for use by the sensor.
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Reset the trigger pin.
GPIO.output(TRIG, 0)
time.sleep(2)

# Continuously...
def getDistance(TRIG, ECHO):
	# Send an ultrasound pulse.
	GPIO.output(TRIG, 1)
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)

	# Detect the echo.
	while GPIO.input(ECHO) == 0:
		pulse_start = time.time()
	while GPIO.input(ECHO) == 1:
		pulse_end = time.time()

	# Calculate the pulse duration.
	pulse_duration = pulse_end - pulse_start

	# Calculate the distance using half the speed of sound in cm.s^-1 in air.
	distance = pulse_duration * 17150

	# Round the distance to 2 decimal places.
	distance = round(distance, 2)

	# Output the distance to the display.
	print("Distance: {0} cm".format(distance))

	# Return the distance value to the program that called the function.
	return distance
	
	# Wait before getting the next pulse.
	time.sleep(0.2)


#while True:
#	getDistance(23, 24)
#	time.sleep(0.1)
