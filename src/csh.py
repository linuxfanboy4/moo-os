import time
import random
import subprocess
import requests

variables = {}

def csh_welcome():
    print("Welcome to Cow's Shell Scripting (CSh)! Type 'exit' to leave.")
    print("You can write MOO-OS Scripting Language code here.")
    print("Supported Commands:")
    print("polishcow('message'); - Prints a message.")
    print("moo('prompt'); - Prompts for user input.")
    print("count - <start> to <end> - Loops a number range.")
    print("polishmath('expression'); - Evaluates math expressions.")
    print("variable = value - Assigns a variable.")
    print("exit - Exits Cow's Shell.")

def execute_csh(command):
    try:
        if "polishcow(" in command:
            message = command.split("polishcow(")[1].split(")")[0].strip().replace('"', '')
            print(message)
        elif "moo(" in command:
            prompt = command.split("moo(")[1].split(")")[0].strip().replace('"', '')
            input(f"{prompt}: ")
        elif "count" in command:
            parts = command.split("count - ")[1].split(" - to ")[0], command.split(" - to ")[1]
            start = int(parts[0])
            end = int(parts[1])
            for i in range(start, end + 1):
                print(i)
        elif "polishmath(" in command:
            expression = command.split("polishmath(")[1].split(")")[0].strip()
            result = eval(expression)
            print(f"Result: {result}")
        elif "=" in command:
            var_name, value = command.split("=")
            var_name = var_name.strip()
            variables[var_name] = value.strip()
            print(f"{var_name} = {value.strip()}")
        elif "printvars" in command:
            print("Variables: ", variables)
        elif "clearvars" in command:
            variables.clear()
            print("All variables cleared.")
        elif "exit" in command:
            return False
        elif "random" in command:
            min_val = int(command.split("random ")[1].split(" to ")[0])
            max_val = int(command.split("to ")[1])
            print(random.randint(min_val, max_val))
        else:
            print("Moo! Unknown command.")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return True

def csh_command():
    csh_welcome()
    while True:
        cmd = input("CSh> ").strip()
        if not execute_csh(cmd):
            break

def main():
    while True:
        cmd = input("CSh> ").strip().lower()
        if cmd == "csh":
            csh_command()
        else:
            print("Unknown command. Type 'csh' to enter the Cow's Shell.")
            
if __name__ == "__main__":
    main()
