#!/usr/bin/env python3
"""
Main code for Robot
"""

import wpilib
import robotmap
import ctre
from wpilib import Joystick
from subsystems.drivetrain import DriveTrain as Drive
from subsystems.grabber import Grabber
from robotpy_ext.autonomous import AutonomousModeSelector


class Robot(wpilib.IterativeRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.pneumaticControlModuleCANID = robotmap.PCM
        self.kDriveTrain = robotmap.DriveTrain
        self.kCubeGrabber = robotmap.CubeGrabber
        self.kSticks = robotmap.Sticks
        self.dStick = Joystick(self.kSticks['drive'])
        self.cStick = Joystick(self.kSticks['control'])
        self.drive = Drive(self)
        self.cubeGrabber = Grabber(self)

        #components to make available to autonomous
        self.components = {
            'drive': self.drive
        }
        #use name of the folder holding our autonomous modes and the name of 
        #the object holding components for autonomous
        self.automodes = AutonomousModeSelector('autonomous', self.components)

    def robotPeriodic(self):
        pass

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        self.drive.stop()

    def autonomousInit(self):
        """
        This function is run once each time the robot enters autonomous mode.
        """
        # get field data
        #self.fielddata = wpilib.DriverStation.getInstance().getGameSpecificMessage()        

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        self.automodes.run()
        #nearswitch, scale, farswitch = list(self.fielddata)
#         
#         if nearswitch == 'R':
#             self.drive.arcade(.5, .2)
#         else:
#             self.drive.arcade(.5, -.2)


    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        speed = self.dStick.getY() * -1
        rotation = self.dStick.getTwist()
        # self.drive.moveSpeed(speed, speed)

        if self.isSimulation():
            self.drive.arcade(speed, rotation)
        else:
            self.drive.arcadeWithRPM(speed, rotation, 2800)

        self.cubeGrabber.grabberFunction()

        # TODO:  need something like this in commands that autonomous or teleop 
        # would run to make sure an exception doesn't crash the code during
        # competition.
        #raise ValueError("Checking to see what happens when we get an exception")



    def testInit(self):
        pass

    def testPeriodic(self):
        wpilib.LiveWindow.setEnabled(True)
        pass
    

if __name__ == "__main__":
    wpilib.run(Robot)
