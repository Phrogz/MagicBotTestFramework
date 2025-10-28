"""Identifiers for objects on the CAN bus(es) and physical robot dimensions."""

from enum import IntEnum
from typing import Final

import wpimath.units as units

# The name of the CAN bus where the swerve modules are connected; configured in Phoenix Tuner X
SWERVE_CAN_NAME: Final[str] = "canivore"


class CANID(IntEnum):
    """IDs for items on the CAN bus."""

    FRONT_LEFT_DRIVE = 1
    FRONT_LEFT_STEER = 2
    FRONT_RIGHT_DRIVE = 3
    FRONT_RIGHT_STEER = 4
    REAR_LEFT_DRIVE = 5
    REAR_LEFT_STEER = 6
    REAR_RIGHT_DRIVE = 7
    REAR_RIGHT_STEER = 8

    SHOOTER_MOTOR = 15


class RobotDimension:
    """Physical dimensions and locations of robot components."""

    # Swerve module locations relative to robot center
    SWERVE_FRONT_LEFT_LOCATION_X: Final[units.meters] = 0.342
    SWERVE_FRONT_LEFT_LOCATION_Y: Final[units.meters] = 0.381
    SWERVE_FRONT_RIGHT_LOCATION_X: Final[units.meters] = 0.342
    SWERVE_FRONT_RIGHT_LOCATION_Y: Final[units.meters] = -0.381
    SWERVE_REAR_LEFT_LOCATION_X: Final[units.meters] = -0.273
    SWERVE_REAR_LEFT_LOCATION_Y: Final[units.meters] = 0.381
    SWERVE_REAR_RIGHT_LOCATION_X: Final[units.meters] = -0.273
    SWERVE_REAR_RIGHT_LOCATION_Y: Final[units.meters] = -0.381

    # Shooter dimensions
    SHOOTER_Z: Final[units.meters] = 0.421
    SHOOTER_MAX_ANGLE: Final[units.radians] = units.degreesToRadians(34.0)


class ControllerPort:
    """USB ports for controllers."""

    DRIVER_CONTROLLER: Final[int] = 0
    OPERATOR_CONTROLLER: Final[int] = 1
