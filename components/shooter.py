import magicbot
import wpilib


class Shooter:
    """Pew! Pew!"""

    shooter_motor: wpilib.Talon

    # speed is tunable via NetworkTables
    shoot_speed = magicbot.tunable(1.0)

    def __init__(self):
        self.enabled = False

    def enable(self):
        """Causes the shooter motor to spin"""
        self.enabled = True

    def is_ready(self):
        # in a real robot, you'd be using an encoder to determine if the
        # shooter were at the right speed..
        return True

    def execute(self):
        """This gets called at the end of the control loop"""
        if self.enabled:
            self.shooter_motor.set(self.shoot_speed)
        else:
            self.shooter_motor.set(0)

        self.enabled = False
