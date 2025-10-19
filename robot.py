import magicbot
import wpilib

import components


class MyRobot(magicbot.MagicRobot):
    our_shooter: components.Shooter

    def createObjects(self):
        """Create motors and stuff here"""

        self.shooter_motor = wpilib.Talon(17)

    def teleopInit(self):
        """Called when teleop starts; optional"""

    def teleopPeriodic(self):
        pass
