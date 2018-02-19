import wpilib

from wpilib import SmartDashboard
from wpilib.buttons import Button

class FROGstick(wpilib.Joystick):
    
    # used to change joystick axis values mathematically in
    # GetX() and GetY()
    # either 1 or 3 (3 is for cubed input)
    _XExponent = 1
    _YExponent = 1
    # booleans to track the state
    YCubed = False
    XCubed = False
    
    # factor to mutiply to the Y axis value.  This is useful
    # This then is used to change the direction of the Y Axis
    # mathematically in Getchanges the direction of the robot
    # in GetY
    _YDirection = -1
    # we have an additional boolean that will tell us
    # which Y axis mode we are in.
    YReversed = False
    
    def __init__(self):
	# initialize with the parent object's init
	super().__init__(self)
    
    
    def GetX(self):
	return super().GetX()**self._XExponent
    
    def GetY(self):
	return (super().GetY() * self._YDirection)**self._YExponent
    
    def ToggleDirection(self):
	# multiply the current value by -1 to change between 1 and -1
	self._YDirection *= -1
	# evalutes to True if _YDirection == 1
	self.YReversed = self._YDirection == 1
	
    # at this point, we only want the possibility of 2 exponents:
    # either 1, for no change, or 3 for a cubed input (that gives)
    # us a more gradual curve at small values of X
    
    def ToggleAttribute(self, attr, value1, value2):
	'''Takes an attribute as an argument and then toggles it between
	the two values given.  this works because we put the two values 
	in a list [value1, value2] and then get one item from the list
	by specifying an index.  In this case the index is created by 
	doing an evaluation (value == 1), which if true, would give us a
	boolean of True and True == a 1 in Python.  Conversely, False
	equals a 0.  Therefore we get an index of 0 or 1 for our string.
	Checking to see if the attribute equals the first value will give
	us a True or 1 evaluation, which is the second value in the list.
	This effectively causes the attribute to toggle between the two
	values every time it's called, assuming the values never change.
	'''
	attr = [value1, value2][attr == value1]
	
    def ToggleXCubed(self):
	self.ToggleAttribute(self._XExponent, 1, 3)
	self.XCubed = self._XExponent == 3
	
    def ToggleYCubed(self):
	self.ToggleAttribute(self._YExponent, 1, 3)
	self.YCubed = self._YExponent == 3
	
    def ToggleCubed(self, AxisExponent):
	self.ToggleXCubed()
	self.ToggleYCubed()

    
class OperatorInterface:

    def __init__(self, robot):

	d_up = Button('')

        # Connect the buttons to commands
		#d_up.whenPressed(SetElevatorSetpoint(robot, 0.2))
		
