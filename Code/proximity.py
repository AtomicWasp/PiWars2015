#!/usr/bin/python

# proximity.py (Proximity Alert) by George P Tuli of Positronic for Pi Wars 2015.

# Import the required libraries.
import PicoBorgRev as p
import xbox
import time
import atexit
import ultrasonic
import math

# Setup the reference to the motor controllers.
p1 = p.PicoBorgRev()
p1.i2cAddress = 10
p1.Init()
p1.ResetEpo()

p2 = p.PicoBorgRev()
p2.i2cAddress = 11
p2.Init()
p2.ResetEpo

# Define the xbox controller object.
pad = xbox.Joystick()

# Auto-disable motors.
def turnOffMotors():
        p1.MotorsOff()
        p2.MotorsOff()
        pad.close()

# Set the exit function to disable motors.
atexit.register(turnOffMotors)

### Motors 1 and 3 must be wired in reverse for the standard setup to function correctly (swap + and - wires). ###

# Clamp motor values to within a specified range minn to maxn.
def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

# Set motor speeds for movement in any direction at any velocity.
def setSpeeds(angle, velocity, rotation):
	# Determine the x and y velocities from the direction of the required movement.
	xVelocity = round(math.sin(math.radians(angle)), 0) * velocity
	yVelocity = round(math.cos(math.radians(angle)), 0) * velocity

	# Set motor speeds.
        A = round(clamp((xVelocity + yVelocity + rotation) * 2, -100, 100), 2)  # Front-left.
        B = round(clamp((xVelocity + (yVelocity * -1) + rotation) * 2, -100, 100), 2)  # Front-right.
        C = round(clamp(((xVelocity * -1) + (yVelocity * -1) + rotation) * 2, -100, 100), 2)  # Back-right.
        D = round(clamp(((xVelocity * -1) + yVelocity + rotation) * 2, -100, 100), 2)  # Back-left.

        A /= 100
        B /= 100
        C /= 100
        D /= 100

        print "A {0}".format(A)
        print "B {0}".format(B)
        print "C {0}".format(C)
        print "D {0}".format(D)
	
	return A, B, C, D

# Start reading the conroller input.
def drive(A, B, C, D):
# Run motor A.
        p1.SetMotor1(A)

        # Run motor B.
        p1.SetMotor2(B)

        # Run motor C.
        p2.SetMotor1(C)

        # Run motor D.
        p2.SetMotor2(D)

# Drive slowly forwards until the distance sensor reads 3 cm.
while ultrasonic.getDistance(23, 24) > 7:
	A, B, C, D = setSpeeds(0, 30, 0)  # Call the setSpeeds function to set the four motor speeds.
	drive(A, B, C, D)
	print("Still")

# Stop because the robot is at the wall.
turnOffMotors()

### End of program.  ###
