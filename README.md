# Gears and Buccaneers FRC Robot Code

Pure Python codebase using [RobotPy](https://robotpy.readthedocs.io/en/stable/)
with the [MagicBot](https://robotpy.readthedocs.io/en/latest/frameworks/magicbot.html) framework.

## Installation

0. If not already installed, install [UV](https://docs.astral.sh/uv/getting-started/installation/)
   and [git](https://git-scm.com/downloads).
   * Not used git before? Be sure to [set your username and email](https://stackoverflow.com/a/33024593/405017).

1. Clone the GitHub repo.

2. In a terminal in the working directory for the cloned files, run:

```sh
uv sync                  # Create a virtual python environment with necessary pre-requisites
source .venv/bin/active  # Activate the virtual environment
robotpy sync             # Install all the robotpy libraries
```

3. Open the folder in VS Code.
   * Though there's little likelihood of conflict, you may wish to create a new VS Code profile with only the recommended VS Code extensions installed.
