"""Controllers for both the driver and operator."""

import wpilib


class OurPS4Controller(wpilib.PS4Controller):
    """A wrapper around wpilib.PS4Controller to provide easier access to common controls."""

    def get_left_stick(self) -> tuple[float, float]:
        """Get the position of the left stick as two values, both in the range [-1.0, 1.0].

        Note:
            Moving the stick to the right is +x, and down is +y.
        """
        return (self.getRawAxis(0), self.getRawAxis(1))

    def get_right_stick(self) -> tuple[float, float]:
        """Get the position of the right stick as two values, both in the range [-1.0, 1.0].

        Note:
            Moving the stick to the right is +x, and down is +y.
        """
        return (self.getRawAxis(2), self.getRawAxis(5))


class DriverController(OurPS4Controller):
    """Controller with information focused on the driver controls."""

    def should_brake(self) -> bool:
        """Determine if the brake button is actively being pressed."""
        return self.getCrossButton()
