from player import *
from item import *
from functions import *
from threat import *
import os
import time


#initialize main character
main_character = Player()

#initialize items
bandage = Bandage('Bandage', 'Clean bandages')
magic_mushroom = Magic_Mushroom('Magic Mushroom', 'Amanita Muscaria- consume with caution')
bear = Bear('Brown Bear', 50, 20)

def get_input(valid_actions):
    global_commands = {
        'quit': quit_game,
        'help': show_help,
        'status': show_status,
        'inventory': show_inventory,
    }
    action = input('>').lower()

    if action in global_commands:
        global_commands[action]()

    elif action.startswith("use "):
        item_name = action[4:] #remove use
        main_character.use_item(item_name)
        get_input()

    elif action.startswith("inspect "):
        item_name = action[8:] #remove inspect
        print(item_name.examine_item)
        get_input()
    
    elif action.startswith("equip ")

    elif action in valid_actions:
        return action
    
    else:
        print(f"Invalid command.. Type 'help' for a list of commands.")


def quit_game():
    print_slow("Quitting the game...")
    time.sleep(2)
    sys.exit()

#print help screen
def show_help():
    print_fast(f"\nAvailable commands: quit, help, status, inventory, use item name, inspect item name, equip weapon name")
    print_fast(f"Other commands vary based on situation..")

#print player status
def show_status():
    print(main_character.player_status())

def show_inventory():
    inventory_str = ', '.join(f"{item.name} (x{item.quantity})" for item in main_character.inventory) if main_character.inventory else 'Empty'
    print(f"inventory_str")

def equip_weapon():

def inspect_item():

def 

#define reusable game header
def game_header():
    #clear terminal
    os.system("cls")
    #game header
    print(f"###################")
    print(f"Wilderness Survival")
    print(f"###################\n")



#setup game and player name
def game_setup():
    game_header()
    print_slow(f"Enter your name to play or quit to exit game")
    #run name_player function to ask for input and save player.name
    main_character.name_player()
    #quit exits game
    if main_character.name.lower() == 'quit':
        quit_game()
    #invalid name check - restarts prompt 
    elif main_character.name.isspace() == 1 or main_character.name == '':
        print(f"Invalid name, please try again..")
        time.sleep(2)
        game_setup()
    #run game_start with name saved
    else:
        game_start()

#choose north or south on trail
def trail_choice():
    choice = input('>')
    if choice.lower() == 'south' or choice.lower() == 's':
        trail_south()
    elif choice.lower() == 'north' or choice.lower() == 'n':
        trail_north()
    else:
        print(f"It's not that complicated.. north or south?")
        trail_choice()

#print header and game intro
def game_start():
    game_header()
    print_slow(f"The trip of a lifetime...")
    print_slow(f"A challenge beyond your experience..")
    print_slow(f'''"You're crazy!".."You won't make it out alive".."Dad, be careful"..''')
    print_slow(".   .   .  ")
    time.sleep(2)
    print_slow(f'''\x1B[3mThree nights into your solo adventure into the forest.. Lost and anxious, you look at your map again.. "Dammit!" Maybe you shouldn't have ventured off-trail\x1B[0m''')
    print_slow(".   .   .  ")
    time.sleep(2)
    print_slow(f"You finally emerge from the woods and stumble onto a narrow deer trail.")
    print_slow(f"This trail is flanked by dense brush on both sides and runs north to south.")
    print_slow(f"Which way will you go?")
    trail_choice()

#heading south down the trail - bear encounter
def trail_south():
    game_header()
    print_slow(f"Traveling south down the trail for several minutes as the sun begins to set to your right.")
    print_slow(f"\x1B[3mI'll need to set up camp soon..\x1B[0m")
    print_slow(f"You see a large dark shape ahead, bent over and consuming something.")
    print_fast(f"It's a fucking bear! What the fuck are you going to do?!")
    bear_choice()

def trail_north():
    game_header()
    print(f"Traveling south down the trail for several minutes as the sun begins to set to your right.")
    print(f"\x1B[3mI'll need to set up camp soon..\x1B[0m")
    print(f"")
    
def bear_choice():
    choice = input(">")
    if choice.lower() == 'fight' or choice.lower() == 'attack':
        print_slow(f"Okay {main_character.name}, you must be a masochist. Good luck fighting the fucking bear..")
        main_character.attack(bear)


#start game - move to play_game?
game_setup()

#def game_start():

    



#main_character.add_item(magic_mushroom, 50)
#magic_mushroom.use(main_character)
#bear.attack(main_character)
#
