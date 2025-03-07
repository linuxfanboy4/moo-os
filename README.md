# MOO-OS: The Most Moo-tivating Operating System

## Overview

MOO-OS is a lightweight, cow-themed operating system built entirely in Python. Designed for **entertainment purposes**, MOO-OS provides a playful environment where users can interact with a variety of cow-themed commands, utilities, and games and it's Default Shell is csh (Cow Shell), Whether you're looking to moo like a cow, play a guessing game, or even simulate a hacking session, MOO-OS has something for everyone.

The system is divided into three main components:
- **Kernel (`kernel.py`)**: Handles core functionalities such as system commands, utilities, and basic operations.
- **User Space (`user-space.py`)**: Provides user-facing commands, games, and network utilities.
- **Cow's Shell (`csh.py`)**: A REPL environment that allows users to write and execute scripts in **Cow's Shell Scripting Language (CSH)**.

MOO-OS is currently at version **v2.1.0** and is actively maintained.

## Features

### Core Commands
- **`moo`**: The OS moos at you!
- **`date`**: Displays the current date and time.
- **`echo`**: Repeats the provided text. Use `echo $SHELL` to see the shell path.
- **`clear`**: Clears the terminal screen.
- **`fortune`**: Displays a random cow-themed fortune.
- **`sysinfo`**: Displays system information about MOO-OS.
- **`storage`**: Shows available storage (fixed at 1 TB for now).
- **`exit`**: Shuts down MOO-OS.
- **`shell`**: Displays the current shell name (default: `csh` - Cow's Shell).

### Cow-Themed Games and Fun
- **`moogame`**: A guessing game where you try to guess the cow's secret number.
- **`moospeak <text>`**: Translates your text into "Moo-speak."
- **`mooweather`**: Provides a cow-themed weather forecast.
- **`moohack`**: Simulates a hacking session with cow-themed humor.
- **`moodisco`**: Starts a cow disco party with colorful text animations.
- **`milkshake`**: A playful command that pretends to blend a milkshake.

### Utilities
- **`cowsay <text>`**: Makes a cow say something (requires installation via `moo eat cowsay`).
- **`calc <expression>`**: A simple calculator for basic arithmetic.
- **`editor`**: A mini text editor for creating and saving text files.
- **`moo eat cowsay`**: Installs the `cowsay` utility.
- **`csh`**: Enters the **Cow's Shell Scripting Language (CSH)** REPL environment.

### Network Utilities
- **`ping <host>`**: Pings a host to check connectivity (default: 8.8.8.8).
- **`download <url>`**: Downloads a file from the internet using a simulated `wget` command.
- **`ip`**: Retrieves and displays your public IP address.

## Cow Shell Scripting Language

MOO-OS introduces **Cow Shell Scripting Language**, a fun and simple scripting language for writing cow-themed scripts. The `csh.py` file provides a REPL environment where users can execute Cow Shell Scripting Language Code

### Supported Commands in Cow Shell Scripting Language 
- **`polishcow('message');`**: Prints a message.
- **`moo('prompt');`**: Prompts for user input.
- **`count - <start> to <end>`**: Loops through a number range.
- **`polishmath('expression');`**: Evaluates math expressions.
- **`variable = value`**: Assigns a variable.
- **`printvars`**: Displays all variables.
- **`clearvars`**: Clears all variables.
- **`random <min> to <max>`**: Generates a random number between `min` and `max`.
- **`exit`**: Exits the Cow's Shell.

### Example CSH Script
```csh
polishcow("Welcome to Cow's Shell!");
moo("Enter your name");
count - 1 to 5;
polishmath("2 + 2 * 2");
random 1 to 10;
exit;
```

## Installation

MOO-OS is easy to install and run. Follow these steps to get started:

1. **Download the Required Files**:
   Use `wget` to download the latest version of MOO-OS from the official repository:
   ```bash
   wget https://raw.githubusercontent.com/linuxfanboy4/moo-os/refs/heads/main/src/kernel.py
   wget https://raw.githubusercontent.com/linuxfanboy4/moo-os/refs/heads/main/src/user-space.py
   wget https://raw.githubusercontent.com/linuxfanboy4/moo-os/refs/heads/main/src/csh.py
   ```

2. **Run MOO-OS**:
   Execute the `user-space.py` file to start MOO-OS:
   ```bash
   python3 user-space.py
   ```

3. **Start Exploring**:
   Once MOO-OS is running, type `help` to see a list of available commands and start exploring the cow-themed world

## Usage Examples

### Basic Commands
- Display the current date and time:
  ```
  MOO-OS> date
  ```

- Clear the terminal screen:
  ```
  MOO-OS> clear
  ```

- Get a random cow-themed fortune:
  ```
  MOO-OS> fortune
  ```

### Games and Fun
- Play the cow guessing game:
  ```
  MOO-OS> moogame
  ```

- Translate text into Moo-speak:
  ```
  MOO-OS> moospeak Hello, world!
  ```

- Simulate a hacking session:
  ```
  MOO-OS> moohack
  ```

### Utilities
- Use the mini text editor:
  ```
  MOO-OS> editor
  ```

- Install the `cowsay` utility:
  ```
  MOO-OS> moo eat cowsay
  ```

- Make a cow say something:
  ```
  MOO-OS> cowsay Hello, MOO-OS!
  ```

- Enter the Cow's Shell:
  ```
  MOO-OS> csh
  ```

### Network Utilities
- Ping a host:
  ```
  MOO-OS> ping google.com
  ```

- Download a file from the internet:
  ```
  MOO-OS> download
  ```

- Retrieve your public IP address:
  ```
  MOO-OS> ip
  ```

## System Requirements

MOO-OS is designed to run on any system with Python 3 installed. It is lightweight and does not require any additional dependencies beyond the Python standard library.

## Contributing

MOO-OS is an open-source project, and contributions are welcome! If you have ideas for new features, bug fixes, or improvements, feel free to fork the repository and submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Submit a pull request.

## License

MOO-OS is released under the **MIT License**. See the `LICENSE` file in the repository for more details.

## Support

For questions, issues, or feature requests, please open an issue on the [GitHub repository](https://github.com/linuxfanboy4/moo-os.git).
