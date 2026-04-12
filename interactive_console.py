import os
import time
import keyboard
from termcolor import colored

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def interactive_menu(options, header = "", color = ""):
    current = 0
    while True:
        time.sleep(0.3)
        clear_console()
        print(colored(header, color))
        for i, option in enumerate(options):
            if i == current:
                print(colored(f"> {option}", "green"))
            else:
                print(f"  {option}")
        key = keyboard.read_key()
        if key == "up":
            current = (current - 1) % len(options)
        elif key == "down":
            current = (current + 1) % len(options)
        elif key == "enter":
            return current

def println(msg, color = "white", speed = "Normal"):
    speeds = {
        "Slow":0.7,
        "Normal":1,
        "Fast":1.5
    }
    for m in msg.split("\n"):
        print(colored(m, color))
        start_time = time.time()
        while time.time() < start_time + max(len(m)/(10*speeds[speed]),2):
            if keyboard.is_pressed("space"):break
        time.sleep(0.05)

