#!/usr/bin/python

# radio_control.py (Control with the Xbox controller) by George P Tuli of Positronic for Pi Wars 2015.

# Import the required libraries.
import PicoBorgRev as p
import xbox
import time
import atexit

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

# Clamp motor values to within the range minn to maxn.
def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

# Start reading the conroller input.
while True:
	xVelocity = pad.leftX(deadzone = 12000) * 100
	yVelocity = pad.leftY(deadzone = 12000) * 100
	rotation = pad.rightX(deadzone = 12000) * 100
	
	# Print the values to the screen (if plugged into HDMI port).
#	print 'X1 value: {0}'.format(xVelocity)
#	print 'Y1 value: {0}'.format(yVelocity)
#	print 'Rotation: {0}\n'.format(rotation)

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

	# Run motor A.
	p1.SetMotor1(A)

	# Run motor B.
	p1.SetMotor2(B)

	# Run motor C.
	p2.SetMotor1(C)

	# Run motor D.
	p2.SetMotor2(D)

# End of program.
