import os  
import datetime  
import random  
import time  
import platform  

MOO_OS_NAME = "moo-os"  
MOO_OS_PATH = f"/data/data/{MOO_OS_NAME}/cow/moo"  
COWSAY_INSTALLED = False  
NOTES_FILE = "moo_notes.txt"  
FORTUNES = [  
    "Moo wisely and fortune will follow.",  
    "The grass is greener where you water it.",  
    "A content cow moos the loudest.",  
    "Don't cry over spilled milk, just moo on.",  
    "A cow that does not moo is a silent udder.",  
    "Moo to your heart’s content!"  
]  

def moo_welcome():  
    print(r"""  
     (__)  
     (oo)  Welcome to the most MOO-tivating OS!  
      \/   Type 'help' for more cow-powered fun.  
    """)  

def moo_command():  
    print("Moooooo! 🐄")  

def date_command():  
    print("Current Date & Time:", datetime.datetime.now())  

def echo_command(text):  
    if text.strip() == "$SHELL":  
        print("MOO-OS Shell")  
    else:  
        print(text)  

def help_command():  
    print("""  
Cow-tastic commands:  
  moogame    - Guess the cow's secret number.  
  moospeak   - Speak like a cow! 'moospeak <text>'  
  mooweather - Cow weather forecast. Moo-rrific!  
  moohack    - Activate fake hacking mode! 🐄💻  
  moodisco   - A cow disco party! Join the Moo-vie!  
  milkshake  - Wanna shake? Moo-ving milkshake!  
  editor     - Open the mini text editor. Type and save your files!  
  sysinfo    - Display system information.  
  storage    - Check available storage.  

Moo Utilities:  
  moo        - The OS moos at you!  
  date       - Shows the current date and time.  
  echo       - Repeats what you say. Use 'echo $SHELL' to see the shell path.  
  cowsay     - Make a cow say something (if installed).  
  moo eat    - Install extra tools (e.g., moo eat cowsay).  
  fortune    - Get random cow wisdom.  
  calc       - Simple calculator (usage: calc 5 + 3).  
  clear      - Clears the screen.  
  exit       - Shuts down MOO-OS. Moo-later!  
  cowsayhelp - Get help for using cowsay.  
""")  

def clear_screen():  
    os.system("cls" if os.name == "nt" else "clear")  

def moogame():  
    print("Guess the cow's secret number between 1 and 10!")  
    secret_number = random.randint(1, 10)  
    while True:  
        guess = input("Your guess? ")  
        if not guess.isdigit():  
            print("Moo? Only numbers!")  
            continue  
        guess = int(guess)  
        if guess == secret_number:  
            print("Mooooo! You win! 🐄🎉")  
            break  
        else:  
            print("Baaad guess! Moo-ve on!")  

def moospeak(text):  
    translated = " ".join(["moo" if c.isalpha() else c for c in text])  
    print(f"Translation to Moo-speak: {translated}")  

def mooweather():  
    conditions = [  
        "Mooing! Sunny ☀️, perfect for grazing.",  
        "Moo... it's raining cows 🌧️. Get your hay!",  
        "A little moo-wind 🌬️. Hold on tight!",  
        "Snowing ❄️... watch out for cold hooves!"  
    ]  
    print(f"Cow Weather: {random.choice(conditions)}")  

def moohack():  
    print("Activating Hack Mode... 🐄💻")  
    time.sleep(1)  
    for i in range(5):  
        print(f"Hacking the farm system... {random.randint(10, 99)}% complete")  
        time.sleep(0.5)  
    print("Moo-hack complete! Your cow data is now secure! 🐄💾")  

def moodisco():  
    colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m", "\033[97m"]  
    for _ in range(10):  
        print(random.choice(colors) + "🎶 Moo Moo Disco Party! 🎶")  
        time.sleep(0.3)  
    print("\033[0mDisco over. Moo-ving on!")  

def milkshake_command():  
    print("Blending your milkshake... Mooo! 🍦🐄")  
    time.sleep(1)  
    print("Wait... Whoops! Just kidding! Moo-lkshakes are for cows only!")  

def fortune_command():  
    print(random.choice(FORTUNES))  

def sysinfo_command():  
    print("System Information:")  
    print("System: MOO-OS")  
    print("Node: localhost")  
    print("Release: March 7 2025")  
    print("Depends: Python")  
    print("Version: 1.7.1+")  
    print("Machine: x86-64 MOO-OS")  
    print("Processor: MOO-OS 0.0.1 Processor")  

def storage_command():  
    print("Storage: 1 TB")  

def cowsayhelp():  
    print("""  
How to use cowsay:  
  To make a cow say something, just type: cowsay "<text>"  
  Example: cowsay "Moo Moo, I'm a cow!"  
""")  

def calculator(expression):  
    try:  
        result = eval(expression)  
        print(f"Result: {result}")  
    except Exception:  
        print("Moo, that didn't work. Try again, math wizard!")  

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

def main():  
    moo_welcome()  

    while True:  
        cmd = input("MOO-OS> ").strip().lower()  

        if cmd == "moo":  
            moo_command()  
        elif cmd == "date":  
            date_command()  
        elif cmd.startswith("echo "):  
            echo_command(cmd[5:])  
        elif cmd == "help":  
            help_command()  
        elif cmd == "clear":  
            clear_screen()  
        elif cmd == "moogame":  
            moogame()  
        elif cmd.startswith("moospeak "):  
            moospeak(cmd[9:])  
        elif cmd == "mooweather":  
            mooweather()  
        elif cmd == "moohack":  
            moohack()  
        elif cmd == "moodisco":  
            moodisco()  
        elif cmd == "milkshake":  
            milkshake_command()  
        elif cmd == "fortune":  
            fortune_command()  
        elif cmd == "sysinfo":  
            sysinfo_command()  
        elif cmd == "storage":  
            storage_command()  
        elif cmd == "cowsayhelp":  
            cowsayhelp()  
        elif cmd.startswith("calc "):  
            calculator(cmd[5:])  
        elif cmd == "editor":  
            mini_text_editor()  
        elif cmd.startswith("cowsay "):  
            if COWSAY_INSTALLED:  
                cowsay(cmd[7:])  
            else:  
                print("Moo! Cowsay is not installed. Use 'moo eat cowsay' to install it.")  
        elif cmd == "moo eat cowsay":  
            moo_eat_cowsay()  
        elif cmd == "exit":  
            print("Moo-later, alligator! 🐄")  
            break  
        else:  
            print("Unknown command. Type 'help' to discover more moo-tastic features!")  

if __name__ == "__main__":  
    main()
