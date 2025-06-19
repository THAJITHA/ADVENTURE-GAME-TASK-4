import random
import json
import os
from colorama import Fore, Style, init

init(autoreset=True)

inventory = []
player_name = ""

# ---------- Save/Load ----------
SAVE_FILE = "savegame.json"

def save_game():
    data = {"inventory": inventory, "player_name": player_name}
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)
    print(Fore.YELLOW + "💾 Game saved!")

def load_game():
    global inventory, player_name
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            inventory = data.get("inventory", [])
            player_name = data.get("player_name", "")
        print(Fore.GREEN + f"✅ Welcome back, {player_name}!")
    else:
        print(Fore.RED + "❌ No saved game found.")

# ---------- Chapters ----------
def intro():
    global player_name
    print(Fore.CYAN + "🎮 WELCOME TO THE QUEST OF SHADOWS")
    player_name = input("🧙‍♂️ Enter your name, adventurer: ")
    print(Fore.CYAN + f"\nHello, {player_name}. You wake up in a foggy forest with a sword beside you.")
    inventory.append("Rusty Sword")
    print(Fore.MAGENTA + "You picked up a Rusty Sword.")
    chapter_one()

def chapter_one():
    print(Fore.BLUE + "\n🌲 Chapter 1: The Forked Path")
    print("You come across a fork in the road:")
    print("1. Go left toward the mountain.")
    print("2. Go right into the valley.")
    choice = input("Choose 1 or 2: ")
    if choice == "1":
        mountain_path()
    elif choice == "2":
        valley_path()
    else:
        print("❌ Invalid choice.")
        chapter_one()

def mountain_path():
    print(Fore.YELLOW + "\n🗻 You climb the mountain and find a shield.")
    inventory.append("Wooden Shield")
    print("🛡️  You acquired a Wooden Shield!")

    # Random event
    print("Suddenly, a goblin appears!")
    event = random.choice(["fight", "run"])
    if event == "fight":
        print(Fore.RED + "⚔️ You fight the goblin!")
        if "Rusty Sword" in inventory:
            print(Fore.GREEN + "You defeat it using your sword!")
            chapter_two()
        else:
            print(Fore.RED + "You had no weapon. You are defeated!")
    else:
        print(Fore.BLUE + "🏃 You run and hide behind a rock.")
        chapter_two()

def valley_path():
    print(Fore.GREEN + "\n🌄 You walk into a peaceful valley.")
    print("You find a potion on the ground.")
    inventory.append("Healing Potion")
    print("🧪 Healing Potion added to inventory!")
    chapter_two()

def chapter_two():
    print(Fore.BLUE + "\n🏰 Chapter 2: The Hidden Castle")
    print("You see a castle in the distance. A guard stops you.")
    if "Wooden Shield" in inventory:
        print(Fore.GREEN + "🛡️ The guard lets you pass, impressed by your gear.")
        final_chapter()
    else:
        print(Fore.RED + "🚫 The guard blocks your path. You must turn back.")
        save_game()

def final_chapter():
    print(Fore.MAGENTA + "\n👑 Final Chapter: The Throne Room")
    print("Inside the castle, you meet the Dark Lord.")
    if "Healing Potion" in inventory:
        print(Fore.GREEN + "💥 You drink the potion and gain strength.")
        print(Fore.YELLOW + "⚔️ You defeat the Dark Lord! YOU WIN!")
    else:
        print(Fore.RED + "😈 The Dark Lord overpowers you. You lose.")
    save_game()

# ---------- Game Menu ----------
def menu():
    print("╔══════════════════════════════════╗")
    print("║     ⚔️ CHOOSE YOUR OWN ADVENTURE     ║")
    print("╚══════════════════════════════════╝")
    print("1. Start New Game")
    print("2. Load Saved Game")
    print("3. Exit")
    option = input("Choose an option: ")
    if option == "1":
        intro()
    elif option == "2":
        load_game()
        chapter_two()
    elif option == "3":
        print("👋 Goodbye, adventurer!")
    else:
        print("❌ Invalid option.")
        menu()

# Run the game
menu()
