import os
import datetime
import random
import time
import platform

MOO_OS_NAME = "moo-os"
MOO_OS_PATH = f"/data/data/{MOO_OS_NAME}/cow/moo"
COWSAY_INSTALLED = False
FORTUNES = [
    "Moo wisely and fortune will follow.",
    "The grass is greener where you water it.",
    "A content cow moos the loudest.",
    "Don't cry over spilled milk, just moo on.",
    "A cow that does not moo is a silent udder.",
    "Moo to your heart’s content!"
]

def moo_command():
    print("Moooooo! 🐄")

def date_command():
    print("Current Date & Time:", datetime.datetime.now())

def echo_command(text):
    if text.strip() == "$SHELL":
        print("MOO-OS Shell")
    else:
        print(text)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def fortune_command():
    print(random.choice(FORTUNES))

def sysinfo_command():
    print("System Information:")
    print("System: MOO-OS")
    print("Node: localhost")
    print("Release: March 7 2025")
    print("Depends: Python")
    print("Version: 2.0.0+")
    print("Machine: x86-64 MOO-OS")
    print("Processor: MOO-OS 0.0.1 Processor")

def storage_command():
    print("Storage: 1 TB")

def cowsay(text):
    cow = r"""
     ______________
    < {message} >
     --------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\\
                    ||----w |
                    ||     ||
    """
    print(cow.format(message=text))

def moo_eat_cowsay():
    global COWSAY_INSTALLED
    print("Moo-eating cowsay... 🍽️")
    time.sleep(1)
    COWSAY_INSTALLED = True
    print("Cowsay is now installed! You can now use 'cowsay' to make cows talk! 🐄💬")

def mini_text_editor():
    print("Welcome to MOO-OS Mini Text Editor! 🐄")
    print("Type your text below. Type 'SAVE' to save and 'EXIT' to exit the editor.")
    content = []
    while True:
        line = input("MOO-EDITOR> ")
        if line.strip().upper() == "SAVE":
            filename = input("Enter the filename to save as: ")
            with open(filename, "w") as file:
                file.write("\n".join(content))
            print(f"File saved as {filename}")
            break
        elif line.strip().upper() == "EXIT":
            print("Exiting editor without saving.")
            break
        else:
            content.append(line)
