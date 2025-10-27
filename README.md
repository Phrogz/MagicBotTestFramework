# Gears and Buccaneers FRC Robot Code

Pure Python codebase using [RobotPy](https://robotpy.readthedocs.io/en/stable/)
with the [MagicBot](https://robotpy.readthedocs.io/en/latest/frameworks/magicbot.html) framework.

## Installation

0. If not already installed, install [UV](https://docs.astral.sh/uv/getting-started/installation/)
   and [git](https://git-scm.com/downloads).
   * Not used git before? Be sure to [set your username and email](https://stackoverflow.com/a/33024593/405017).

1. Clone the GitHub repo. One way is to run this command in a terminal:

   ```sh
   git clone git@github.com:Phrogz/MagicBotTestFramework.git
   ```

2. In a terminal in the working directory for the cloned files (hint: `cd MagicBotTestFramwork`), run:

   ```sh
   uv sync             # Create a virtual python environment with necessary pre-requisites
   uv run robotpy sync # Install all the robotpy libraries
   ```

3. Open the folder in VS Code.
   * Though there's little likelihood of conflict, you may wish to create a new VS Code profile with only the recommended VS Code extensions installed.

4. From a Terminal in VS Code, run `robotpy sim` to start the simulator.

   * _Note that when you open a Terminal inside VS Code it should automatically activate the virtual environment for you._
     _At this point you can just run `robotpy sync` or `robotpy deploy` without the `uv run` prefix._
     _If the it does not activate the virtual environment automatically, you can run `source .venv/bin/activate`._ 🤮

   * If you connect a PS4 controller, you should be able to drive the robot around in the simulator using the left and right sticks.
     Note that you need to drag the controller from the "System Joysticks" window onto "Joystick 0" in the "Joysticks" window to connect the controller to the right joystick "port".