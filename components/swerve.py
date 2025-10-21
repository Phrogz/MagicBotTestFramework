"""Classes related to Serve drive."""

import dataclasses
from typing import Literal

import phoenix6.hardware as p6
import wpimath.geometry as geom

import dimensions as dim


# TODO: see https://github.com/robotpy/examples/blob/main/SwerveBot/swervemodule.py
class SwerveModule:
    """A single serve module."""

    # These attributes are automatically set by MagicBot's variable injection
    # when attributes of the same name are set on the robot.
    drive_motor: p6.TalonFX
    steer_motor: p6.TalonFX

    def execute(self) -> None:
        """Send commands to the motors to effect requested actions."""
        pass


@dataclasses.dataclass
class DesiredVelocity:
    """Target velocities for the drive train."""

    x: float = 0.0  # longitudinal in m/s; positive = forwards
    y: float = 0.0  # lateral in m/s; positive = left
    r: float = 0.0  # angular in radians/s; positive = counterclockwise


# TODO: see https://github.com/robotpy/examples/blob/main/SwerveBot/drivetrain.py
class Drivetrain:
    """The full drivetrain."""

    # These attributes are automatically populated by MagicBot's variable injection
    # when variables of the same name are set on the robot.
    front_left_swerve: SwerveModule
    front_right_swerve: SwerveModule
    rear_left_swerve: SwerveModule
    rear_right_swerve: SwerveModule

    def __init__(self):
        """Initialize the drivetrain."""
        self.front_left_loc = geom.Translation2d(dim.SWERVE_FRONT_LEFT_LOCATION_X, dim.SWERVE_FRONT_LEFT_LOCATION_Y)
        self.front_right_loc = geom.Translation2d(dim.SWERVE_FRONT_RIGHT_LOCATION_X, dim.SWERVE_FRONT_RIGHT_LOCATION_Y)
        self.rear_left_loc = geom.Translation2d(dim.SWERVE_REAR_LEFT_LOCATION_X, dim.SWERVE_REAR_LEFT_LOCATION_Y)
        self.rear_right_loc = geom.Translation2d(dim.SWERVE_REAR_RIGHT_LOCATION_X, dim.SWERVE_REAR_RIGHT_LOCATION_Y)
        self.desired_velocity = DesiredVelocity()

    def drive(self, *, x_speed: float = 0, y_speed: float = 0, r_speed: float = 0) -> None:
        """Drive the robot.

        Args:
            x_speed: Speed in the longitudinal direction; positive = forwards.
            y_speed: Speed in the lateral direction; positive = left.
            r_speed: Angular speed; positive = counterclockwise seen from above.
        """
        self.desired_velocity.x = x_speed
        self.desired_velocity.y = y_speed
        self.desired_velocity.r = r_speed

    def execute(self) -> None:
        """Called by MagicBot; cause action for queued up control information."""
        # TODO: control the swerve modules to try and achieve the desired_velocity
        pass
