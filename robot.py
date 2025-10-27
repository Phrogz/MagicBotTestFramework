"""Starting point for Robot code."""

import magicbot
import phoenix6.hardware as p6
import wpilib

import components
import components.can_ids as ids


class Scurvy(magicbot.MagicRobot):
    """The main class for the robot."""

    drivetrain: components.Drivetrain
    front_left_swerve: components.SwerveModule
    front_right_swerve: components.SwerveModule
    rear_left_swerve: components.SwerveModule
    rear_right_swerve: components.SwerveModule
    pewpew: components.Shooter
    driver_controller: components.DriverController

    # ------------------------------------------------------------------------------------------------------------------
    # MagicBot methods called at the right time; implement these as desired.
    # ------------------------------------------------------------------------------------------------------------------

    def createObjects(self) -> None:
        """Create motors and stuff here."""
        self.createMotors()
        self.createControllers()
        self.createLights()

    def autonomousInit(self) -> None:
        """Called when auto starts (regardless of which one is selected), after every components' on_enable()."""
        pass

    def teleopInit(self) -> None:
        """Called when teleop starts, after all components' on_enable()."""
        pass

    def teleopPeriodic(self) -> None:
        """Called periodically during teleop (and autonomous, if `self.use_teleop_in_autonomous==True`).

        Called before all components' execute().
        """
        self.manuallyDrive()  # Assumes we always want to drive manually in teleop

    def disabledInit(self) -> None:
        """Called afer the on_disable() of all components."""
        pass

    def disabledPeriodic(self) -> None:
        """Called periodically while the robot is disabled, before all components' execute()."""
        pass

    def testInit(self) -> None:
        """Called when starting test mode."""
        pass

    def testPeriodic(self) -> None:
        """Called periodically while in test mode."""
        pass

    def robotPeriodic(self) -> None:
        """Called periodically regardless of mode, after the mode-specific xxxPeriodic() is called."""
        pass

    # ------------------------------------------------------------------------------------------------------------------
    # Helper methods
    # ------------------------------------------------------------------------------------------------------------------

    def createMotors(self) -> None:
        """Instantiate all the motors."""
        # Because the robot has a component named `front_left_swerve`,
        # and that class has an attribute `drive_motor`,
        # the next line automatically sets the drive_motor value on the specific swerve component.
        self.front_left_swerve_drive_motor = p6.TalonFX(ids.FRONT_LEFT_DRIVE_ID, ids.SWERVE_CAN_NAME)
        self.front_left_swerve_steer_motor = p6.TalonFX(ids.FRONT_LEFT_STEER_ID, ids.SWERVE_CAN_NAME)
        self.front_right_swerve_drive_motor = p6.TalonFX(ids.FRONT_RIGHT_DRIVE_ID, ids.SWERVE_CAN_NAME)
        self.front_right_swerve_steer_motor = p6.TalonFX(ids.FRONT_RIGHT_STEER_ID, ids.SWERVE_CAN_NAME)
        self.rear_left_swerve_drive_motor = p6.TalonFX(ids.REAR_LEFT_DRIVE_ID, ids.SWERVE_CAN_NAME)
        self.rear_left_swerve_steer_motor = p6.TalonFX(ids.REAR_LEFT_STEER_ID, ids.SWERVE_CAN_NAME)
        self.rear_right_swerve_drive_motor = p6.TalonFX(ids.REAR_RIGHT_DRIVE_ID, ids.SWERVE_CAN_NAME)
        self.rear_right_swerve_steer_motor = p6.TalonFX(ids.REAR_RIGHT_STEER_ID, ids.SWERVE_CAN_NAME)

        self.shooter_motor = wpilib.Talon(15)

    def createControllers(self) -> None:
        """Set up joystick and gamepad objects here."""
        self.driver_controller = components.DriverController(0)

    def createLights(self) -> None:
        """Set up CAN objects for lights."""
        pass

    def manuallyDrive(self) -> None:
        """Drive the robot based on controller input."""
        # Translate joystick values to speeds
        strafe_right, forward = self.driver_controller.getLeftStick()
        rotate_right = self.driver_controller.getRightX()
        self.drivetrain.drive(x_speed=-forward, y_speed=-strafe_right, r_speed=-rotate_right)
        self.drivetrain.use_cross_brake(self.driver_controller.should_brake())
