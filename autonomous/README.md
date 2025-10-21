# Adding Auto Modes

To add a new auto mode for the robot:

1. Add a python file in this folder,
2. that defines a class,
3. which has a `MODE_NAME` attribute set to a string,
4. and which implements methods `on_enable()`, `on_iteration()`, and `on_disable()`.

   ```python
   class TheBestAutoEver:
       MODE_NAME = "The Bestest Auto That Rules"

       def on_enable(self):
           """Called when the auto mode starts."""
           pass

       def on_iteration(self):
           """Called periodically during the auto mode."""
           pass

       def on_disable(self):
           """Called when the auto mode ends."""
           pass
   ```

For more details, read the documentation on
_[Autonomous Mode](https://robotpy.readthedocs.io/en/stable/frameworks/magicbot.html#autonomous-mode)_.