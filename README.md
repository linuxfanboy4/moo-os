# MOO-OS: A Whimsical Operating System

## Overview
MOO-OS is a playful, cow-themed operating system designed for entertainment and lighthearted fun. This Python-based system offers a variety of commands and features that blend humor, creativity, and functionality. Dive into the whimsical world of MOO-OS and discover an operating system like no other.

## Key Features
- **Moo-inspired Commands**: Engage with commands that embody the spirit of a cow-themed OS, from mooing to weather forecasts.
- **Mini Games**: Play guessing games and enjoy lighthearted entertainment.
- **Text Editor**: A simple and efficient built-in text editor for quick note-taking.
- **Fake Hacking Mode**: Explore a humorous take on "hacking," complete with percentage progressions.
- **Fun and Functional Utilities**: Execute basic system tasks while having fun with the quirky features.
- **Customizable Cow Sayings**: Install additional tools like `cowsay` to give your cows a voice.
- **Random Fortune Generator**: Gain wisdom from cow-themed sayings.

## Prerequisites
To run MOO-OS, you'll need:
- Python 3.6 or later installed on your system.

## Installation
Follow these steps to install and launch MOO-OS:
1. Download the script:
   ```bash
   wget https://raw.githubusercontent.com/linuxfanboy4/moo-os/refs/heads/main/moo.py
   ```
2. Run the script:
   ```bash
   python moo.py
   ```

## Usage
Once MOO-OS is running, you can interact with it using a variety of commands. Below are some of the key commands and their functions.

### Basic Commands
| Command      | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `moo`        | The OS will moo at you.                                                    |
| `date`       | Displays the current date and time.                                        |
| `echo <text>`| Repeats back the provided text.                                            |
| `help`       | Lists all available commands and their descriptions.                      |
| `exit`       | Shuts down MOO-OS.                                                        |

### Entertainment Commands
| Command        | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `moogame`      | Play a number-guessing game with the cow.                                  |
| `mooweather`   | Displays a humorous weather forecast.                                      |
| `moohack`      | Simulates a fake hacking scenario for laughs.                              |
| `moodisco`     | Activates a simulated disco party in the terminal.                        |
| `milkshake`    | Provides a humorous response about milkshakes.                            |

### Utilities
| Command         | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| `sysinfo`       | Displays system information.                                               |
| `storage`       | Shows available storage space.                                             |
| `calc <expr>`   | A basic calculator to solve arithmetic expressions (e.g., `calc 5 + 3`).   |
| `editor`        | Opens a minimalistic text editor.                                          |
| `fortune`       | Provides a random cow-themed fortune.                                      |

### Customization
| Command             | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `cowsay <text>`     | Displays a cow saying the provided text (requires `cowsay` to be installed).|
| `moo eat cowsay`    | Installs the `cowsay` feature for customizable cow sayings.                 |
| `cowsayhelp`        | Displays help information about the `cowsay` feature.                      |

## Project Structure
The script is written entirely in Python and uses built-in modules for functionality. It includes features like:
- Random number generation using the `random` module.
- Time-based actions using the `time` module.
- Simple text handling and file operations.

## Development and Contribution
Feel free to contribute to MOO-OS by forking the repository and submitting pull requests. All contributions are welcome to make MOO-OS even more feature-rich and fun!
