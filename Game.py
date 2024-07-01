import random
import time

player_types = {
    'Elf': {'health': 80, 'attack': 15, 'defense': 5},
    'Wizard': {'health': 70, 'attack': 20, 'defense': 4},
    'Horse Archer': {'health': 90, 'attack': 12, 'defense': 6},
    'Warrior': {'health': 120, 'attack': 10, 'defense': 8},
    'Paladin': {'health': 110, 'attack': 14, 'defense': 7},
    'Monk': {'health': 100, 'attack': 10, 'defense': 10}
}

player = {
    'name': '',
    'type': '',
    'health': 100,
    'attack': 10,
    'defense': 5,
    'score': 0,
    'experience': 0,
    'level': 1
}

enemies = [
    {'name': 'Goblin', 'health': 30, 'attack': 5, 'defense': 2},
    {'name': 'Troll', 'health': 50, 'attack': 10, 'defense': 5},
    {'name': 'Dragon', 'health': 100, 'attack': 20, 'defense': 10}
]
def set_player_type(choice):
    global player
    if choice == '1':
        player['type'] = 'Elf'
    elif choice == '2':
        player['type'] = 'Wizard'
    elif choice == '3':
        player['type'] = 'Horse Archer'
    elif choice == '4':
        player['type'] = 'Warrior'
    elif choice == '5':
        player['type'] = 'Paladin'
    elif choice == '6':
        player['type'] = 'Monk'
    else:
        print("Invalid choice. Defaulting to Warrior.")
        player['type'] = 'Warrior'

def start_game():
    print("Welcome to the game")
    name = input("Enter your character's name: ")
    print("Choose your class:")
    print("1. Elf")
    print("2. Wizard")
    print("3. Horse Archer")
    print("4. Warrior")
    print("5. Paladin")
    print("6. Monk")
    choice = input("Enter the number corresponding to your choice: ")
    set_player_type(choice)
    player['name'] = name
    player['health'] = player_types[player['type']]['health']
    player['attack'] = player_types[player['type']]['attack']
    player['defense'] = player_types[player['type']]['defense']
    print("Hello! Your Journey begins now")
    game_menu()

def game_menu():
    while True:
        print("1. Explore")
        print("2. Check Stats")
        print("3. Quit")
        choice = input("What would you like to do? (1-3): ")
        if choice == '1':
            explore()
        elif choice == '2':
            check_stats()
        elif choice == '3':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please choose again.")

def explore():
    print("You venture into the lands between")
    time.sleep(1)
    if random.choice([True, False]):
        encounter_enemy()
    else:
        print("You find nothing of interest.")

def encounter_enemy():
    enemy = random.choice(enemies)
    print(f"A wild {enemy['name']} appears!")
    while enemy['health'] > 0 and player['health'] > 0:
        action = input("Do you want to (a)ttack or (r)un away? ")
        if action == 'a':
            attack_enemy(enemy)
        elif action == 'r':
            print("You successfully ran away!")
            break
        else:
            print("Invalid choice.")
    if player['health'] <= 0:
        print("You have been defeated. Game Over.")
        exit()
    elif enemy['health'] <= 0:
        print("You have defeated the enemy!")
        gain_experience(10)
        player['score'] += 10

def attack_enemy(enemy):
    damage_to_enemy = max(0, player['attack'] - enemy['defense'])
    damage_to_player = max(0, enemy['attack'] - player['defense'])
    enemy['health'] -= damage_to_enemy
    player['health'] -= damage_to_player
    print(f"You dealt {damage_to_enemy} damage to the {enemy['name']}.")
    print(f"The {enemy['name']} dealt {damage_to_player} damage to you.")
    if enemy['health'] < 0:
        enemy['health'] = 0
    if player['health'] < 0:
        player['health'] = 0

def check_stats():
    print(f"\nName: {player['name']}")
    print(f"Class: {player['type']}")
    print(f"Health: {player['health']}")
    print(f"Attack: {player['attack']}")
    print(f"Defense: {player['defense']}")
    print(f"Score: {player['score']}")
    print(f"Experience: {player['experience']}")
    print(f"Level: {player['level']}")

def gain_experience(points):
    player['experience'] += points
    if player['experience'] >= 100:
        player['experience'] = 0
        player['level'] += 1
        print(f"Congratulations! You've reached level {player['level']}!")
        level_up()

def level_up():
    player['health'] += 20
    player['attack'] += 5
    player['defense'] += 3
    print("Your stats have increased.")
start_game()






















