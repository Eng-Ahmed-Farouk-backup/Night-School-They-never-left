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

def uni_interactive_menu(options, header = "", color = ""):
    current = 0
    while True:
        clear_console()
        print(colored(header, color))
        for i, option in enumerate(options):
            if i == current:
                print(colored(f">  {option}", "green"))
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


def shop(items, player, diff):
    diffs = {
        "Easy":3,
        "Normal":2,
        "Hard":1
    }

    while True:
        if player.honor < -5 * (diffs[diff]):
            println("You enter the Shop")
            println("The merchant tells you to go away (your honor is too low)")
            return
        options = ["Buy","Sell","Exit"]
        option = interactive_menu(options, "Welcome to the shop!", "yellow")
        if option == 2:
            println("You leave the shop.", "yellow")
            break
        elif option == 0:
            while True:
                item_options = [f"{item.name} - {item.buy_price} gold" for item in items]
                item_options.append("Back")
                item_option = interactive_menu(item_options, "What would you like to buy?", "yellow")
                if item_option == len(item_options)-1:
                    break
                else:
                    if player.gold < items[item_option].buy_price:
                        println("You don't have enough gold to buy that item.", "red")
                        continue
                    else:
                        player.gold -= items[item_option].buy_price
                        println(f"You bought {items[item_option].name} for {items[item_option].buy_price} gold.", "green")
                        player.inventory.append(items[item_option])
        elif option == 1:
            while True:
                item_options = [f"{item.name} - {item.sell_price} gold" for item in player.inventory]
                item_options.append("Back")
                item_option = interactive_menu(item_options, "What would you like to sell?", "yellow")
                if item_option == len(item_options)-1:
                    break
                else:
                    player.gold += player.inventory[item_option].sell_price
                    println(f"You sold {player.inventory[item_option].name} for {player.inventory[item_option].sell_price} gold.", "green")
                    player.inventory.pop(item_option)


def fight(player, enemy):
    println(f"You encounter {enemy.name}!", "red")
    while player.is_alive() and enemy.is_alive():
        println(f"Your HP: {player.get_hp()} | {enemy.name} HP: {enemy.get_hp()}", "yellow")
        options = ["Attack","Run"]
        option = interactive_menu(options, "What would you like to do?", "yellow")
        if option == 0:
            damage = max(0, player.get_attack() - enemy.get_defense())
            enemy.take_damage(damage)
            println(f"You attack {enemy.name} for {damage} damage!", "green")
            if enemy.is_alive():
                damage = max(0, enemy.get_attack() - player.get_defense())
                player.take_damage(damage)
                println(f"{enemy.name} attacks you for {damage} damage!", "red")
        elif option == 1:
            println(f"You run away! you lose {enemy.lost_honor} honor", "yellow")
            player.honor -= enemy.lost_honor
            break
    if not player.is_alive():
        println("You have been defeated!", "red")
    elif not enemy.is_alive():
        println(f"You have defeated {enemy.name}!", "green")
        player.gold += enemy.gold_drop
        player.honor += enemy.honor_drop
        player.inventory.extend(enemy.drop())