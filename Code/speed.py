#!/usr/bin/python

# speed.py (Hand-controlled Speed. Use the forward of the left trigger to move robot forwards at full velocity. Use the left and right of the right trigger to correct) by George P Tuli of Positronic for Pi Wars 2015.

# Import the required libraries.
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import xbox
import time
import atexit

# Define the motor HAT object.
mh = Adafruit_MotorHAT(addr=0x60)

# Define the xbox controller object.
pad = xbox.Joystick()

# Auto-disable motors.
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
	pad.close()

# Set the exit function to disable motors.
atexit.register(turnOffMotors)

# Setup the 4 motors.
M1 = mh.getMotor(1)  # Front-left (A).
M2 = mh.getMotor(2)  # Front-right (B).
M3 = mh.getMotor(3)  # Back-right (C).
M4 = mh.getMotor(4)  # Back-left (D).

### Motors 1 and 3 must be wired in reverse for the standard setup to function correctly (swap + and - wires). ###

# Clamp motor values to within the range minn to maxn.
def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

# Start reading the conroller input.
while True:
	xVelocity = pad.rightX(deadzone = 12000) * 255
	yVelocity = pad.leftY(deadzone = 12000) * 255
	rotation = pad.leftX(deadzone = 12000) * 255
	
	if yVelocity > 0:
		yVelocity = 255
	
	# Set motor speeds.
        A = int(clamp((xVelocity + yVelocity + rotation) * 2, -255, 255))  # Front-left.
        B = int(clamp((xVelocity + (yVelocity * -1) + rotation) * 2, -255, 255))  # Front-right.
        C = int(clamp(((xVelocity * -1) + (yVelocity * -1) + rotation) * 2, -255, 255))  # Back-right.
        D = int(clamp(((xVelocity * -1) + yVelocity + rotation) * 2, -255, 255))  # Back-left.

	# Run motor A.
	if A > 0:
		M1.run(Adafruit_MotorHAT.FORWARD)
		M1.setSpeed(A)
	else:
		M1.run(Adafruit_MotorHAT.BACKWARD)
		M1.setSpeed(A * -1)

	# Run motor B.
	if B > 0:
		M2.run(Adafruit_MotorHAT.FORWARD)
		M2.setSpeed(B)
	else:
		M2.run(Adafruit_MotorHAT.BACKWARD)
		M2.setSpeed(B * -1)

	# Run motor C.
	if C > 0:
		M3.run(Adafruit_MotorHAT.FORWARD)
		M3.setSpeed(C)
	else:
		M3.run(Adafruit_MotorHAT.BACKWARD)
		M3.setSpeed(C * -1)

	# Run motor D.
	if D > 0:
		M4.run(Adafruit_MotorHAT.FORWARD)
		M4.setSpeed(D)
	else:
		M4.run(Adafruit_MotorHAT.BACKWARD)
		M4.setSpeed(D * -1)

# End of program.
