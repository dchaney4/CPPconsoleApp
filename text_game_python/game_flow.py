import os
import time

from item import *
from player import *
from functions import *
from threat import *



######Need to add a search input to global commands
######Need to add a nearby_items function
######Setup attack function


#initialize main character
main_character = Player()

#initialize items
bandage = Bandage()
magic_mushroom = Magic_Mushroom()
bear = Bear()



#########~~Input function and commands~#########

#input with unique actions and error codes
def get_input(valid_actions, error_message = "Invalid command.. Type 'help' for a list of commands."):
    global_commands = { 
        'quit': quit_game,
        'help': show_help,
        'status': show_status,
        'inventory': show_inventory,
    }
    while True:
        action = input('>').lower() #convert to lowercase
    
        if action in global_commands: #check global commands first
            global_commands[action]()
    
        elif action.startswith("use "): #use item input
            item_name = action[4:] #remove use
            main_character.use_item(item_name)

######################Should this be built into the inspect function in item?
        elif action.startswith("inspect "): #inspect item input
            item_name = action[8:] #remove inspect
            main_character.inspect_item(item_name)

        elif action.startswith("equip "): #equip weapon input
            item_name = action[6:] #remove equip
            main_character.equip_weapon(item_name)

        #check instance specific valid_actions
        elif action in valid_actions:
            return action

        #print custom error message or default
        else:
            print(error_message)


        continue

#quit input
def quit_game():
    print_slow("Quitting the game...")
    time.sleep(2)
    sys.exit()

#print help screen input
def show_help():
    print(f"\n(Available commands: quit, help, status, inventory, use item name, inspect item name, equip weapon name)")
    print(f"Other commands vary based on situation..")

#print player status input
def show_status():
    print(main_character.player_status())

#show inventory input
def show_inventory():
    inventory_str = ', '.join(f"{item.name} (x{item.quantity})" for item in main_character.inventory) if main_character.inventory else 'Empty'
    print(inventory_str)


#define reusable game header
def game_header():
    #clear terminal
    print("\n" * 100)
    #game header
    print(f"###################")
    print(f"Wilderness Survival")
    print(f"###################\n")



#setup game and player name
def game_setup():
    game_header()
    print_slow(f"Enter your name to play or quit to exit game.")
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
    choice = get_input(['north', 'south'], "It's not that complicated.. north or south?")
    
    if choice == 'south' or choice == 's':
        trail_south()
    elif choice == 'north' or choice == 'n':
        trail_north()
    else:
        print(error_message)
        trail_choice()

#print header and game intro
def game_start():
    game_header()
    #print_slow(f"The trip of a lifetime...")
    #print_slow(f"A challenge beyond your experience..")
    #print_slow(f'''"You're crazy!".."You won't make it out alive".."Dad, be careful"..''')
    #print_slow(".   .   .  ")
    #time.sleep(2)
    #print_slow(f'''\x1B[3m~Three nights since you had set out on a solo adventure into the forest.. Lost and anxious, you look at your map again..~''')
    #print_slow(f'''~"Dammit!" Maybe you shouldn't have ventured off-trail~\x1B[0m''')
    #print_slow(".   .   .  ")
    #time.sleep(2)
    #print_slow(f"You finally emerge from the woods and stumble onto a narrow deer trail.")
    #print_slow(f"This trail is flanked by dense brush on both sides and runs north to south.")
    main_character.add_item(magic_mushroom, 5)
    print_slow(f"Which way will you go?")
    trail_choice()

#heading south down the trail - bear encounter
def trail_south():
    game_header()
    #print_slow(f"Traveling south down the trail for several minutes as the sun begins to set to your right.")
    #print_slow(f"\x1B[3m~I'll need to set up camp soon..~\x1B[0m")
    #print_slow(f"You see a large dark shape ahead, bent over and consuming something.")
    print_fast(f"Oh shit, it's a bear! What are you going to do?!")
    bear_choice()

def trail_north():
    game_header()
    #print(f"Traveling north down the trail for several minutes as the sun begins to set to your right.")
    #print(f"\x1B[3m~I'll need to set up camp soon..~\x1B[0m")
    print(f"")

#######################utilize the get_input function
def bear_choice():
    choice = get_input(['run', 'fight', 'attack', 'die'], "Hint: trying running shithead")
    if choice == 'fight' or choice == 'attack':
        print_slow(f"Okay {main_character.name}, you must be a masochist then. Good luck fighting the fucking bear..")
        #main_character.attack(bear)
    elif choice == 'die':
        print_slow(f"No honor in suicide by bear..")
        while(True):
            bear.attack(main_character)
    else:
        print_slow(choice.error_message)
        bear_choice()

#start game - move to play_game?
if __name__ == "__main__":
    game_setup()

#def game_start():

    



#main_character.add_item(magic_mushroom, 5)
#magic_mushroom.use(main_character)
#bear.attack(main_character)
#
