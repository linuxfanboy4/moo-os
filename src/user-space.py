import time
import random
import subprocess
import requests
from kernel import *
import csh

def moo_welcome():
    print(r"""    
     (__)    
     (oo)  Welcome to the most MOO-tivating OS!    
      \/   Type 'help' for more cow-powered fun.    
    """)

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
  shell      - Show the current shell name.  

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

Network Utilities:  
  ping <host>  - Ping a host to check connectivity (default: 8.8.8.8).  
  download <url>  - Download a file from the internet using wget.  
  ip             - Get the current public IP address.  
  csh            - Enter the Cow's Shell (CSh).  
""")

def shell_command():
    print("csh (Cow's Shell)")

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

def calculator(expression):  
    try:  
        result = eval(expression)  
        print(f"Result: {result}")  
    except Exception:  
        print("Moo, that didn't work. Try again, math wizard!")

def ping_command(host="8.8.8.8"):  
    print(f"Pinging {host}...")  
    try:  
        response = subprocess.run(  
            ["ping", "-c", "4", host],  
            stdout=subprocess.PIPE,  
            stderr=subprocess.PIPE,  
            text=True  
        )  
        print(response.stdout)  
    except Exception as e:  
        print(f"Error pinging {host}: {e}")

def download_file(url, filename):  
    try:  
        print(f"Downloading file from {url}...")  
        response = requests.get(url)  
        if response.status_code == 200:  
            with open(filename, "wb") as file:  
                file.write(response.content)  
            print(f"File downloaded successfully as {filename}.")  
        else:  
            print(f"Failed to download file. HTTP Status Code: {response.status_code}")  
    except Exception as e:  
        print(f"Error downloading file: {e}")

def ip_command():  
    try:  
        response = requests.get("https://api.ipify.org")  
        if response.status_code == 200:  
            print(f"Your public IP address is: {response.text}")  
        else:  
            print("Failed to retrieve IP address.")  
    except Exception as e:  
        print(f"Error fetching IP address: {e}")

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
        elif cmd == "ping":  
            ping_command()  
        elif cmd.startswith("ping "):  
            host = cmd[5:].strip()  
            ping_command(host)  
        elif cmd == "download":  
            url = input("Enter the URL to download from: ").strip()  
            filename = input("Enter the filename to save as: ").strip()  
            download_file(url, filename)  
        elif cmd == "ip":  
            ip_command()  
        elif cmd == "shell":  
            shell_command()  
        elif cmd == "csh":  
            csh.csh_command()  
        else:  
            print("Unknown command. Type 'help' to discover more moo-tastic features!")

if __name__ == "__main__":  
    main()
