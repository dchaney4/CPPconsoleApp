from item import *
from functions import *


class Player:
    def __init__(self):
        self.name = ''
        self.health = 100
        self.max_health = 100
        self.hunger = 100
        self.max_hunger = 100
        self.inventory = []

    def name_player(self):
        self.name = input('>')
        
    def player_status(self):
        status = f"Name: \033[1;32;40m{self.name}\033[0m Health:     \033[1;31;40m{self.health}/{self.max_health}\033[0m Hunger: \033[1;33;40m{self.hunger}/{self.max_hunger}\033[0m"
        return status
        
    def add_item(self, item, quantity):
        self.inventory.append(item)
        item.quantity = quantity
        if item.quantity > 1:
            print_slow(f"{item.quantity} {item.name}s added to inventory.")
        else:
            print_slow(f"{item.quantity} {item.name} added to inventory.")
        
    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def take_damage(self, damage):
        self.health = self.health - damage
        print_slow(f"\033[1;31m{self.name} took {damage} points of damage.\033[0m")
        if self.health < 75 and self.health >= 50:
            print_slow(f"\033[1;33m'Tis but a scratch\033[0m")
        elif self.health < 50 and self.health >= 25:
            print_slow(f"\033[1;31mUhh, you are supposed to stay alive remember\033[0m")
        elif self.health < 25 and self.health > 0:
            print_slow(f"\033[0;31mYou are going to die out here and no one will find your body..\033[0m")
            print_slow(f"\033[0;31m{self.name} is dead.\033[0m\nBetter luck next time.")
            exit()

    def reduce_hunger(self, amount):
        self.hunger = self.hunger - amount
        if self.hunger < 75 and self.hunger >= 50:
            print_slow(f"Your stomach begins to rumble.")
        elif self.hunger < 50 and self.hunger >= 25:
            print_slow(f"That would be embarrasing to die of hunger..")
        elif self.hunger < 25:
            print_slow(f"You are starving! Should've packed more granola.")

    def gain_hunger(self, amount):

        if self.hunger == self.max_hunger:
            print_slow(f"{self.name} is full. 0 hunger gained.")
        
        elif amount > 1:
            self.hunger = self.hunger + amount
            print_slow(f"\033[0;32m{self.name} gained {amount} points of hunger.\033[0m")
        elif amount == 1:
            self.hunger = self.hunger + amount
            print_slow(f"\033[0;32m{self.name} gained {amount} point of hunger.\033[0m")
        else:
            print_slow(f"{self.name} gained nothing")

    def use_item(self, item_name):

        #vowel checker
        vowels = 'aeiou'
        article = 'an' if item_name[0].lower() in vowels else 'a'

        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                item.use(self)
            else:
                print_slow(f"You do not have {article} {item_name} in your inventory")
            






    def inspect_item(self, item_name):

        #checking for vowels
        vowels = 'aeiou'
        article = 'an' if item_name[0].lower() in vowels else 'a'
        
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                print_slow(item.description)
                return
            else:
                print(f"You do not have {article} {item_name} in your inventory.")

    def equip_weapon(self, item_name):

        #checking for vowels
        vowels = 'aeiou'
        article = 'an' if item_name[0].lower() in vowels else 'a'
        
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                if item.type == 'weapon':
                    
                    self.equipped_weapon = item
                    print_slow(f"You have equipped {article} {item.name}.")
                    return
                else:
                    print_slow(f"{item.name} is not a weapon.")
                    return

        print(f"You do not have {article} {item_name} in your inventory.")
            
    #def attack(self, target):
        #self.equipped_weapon = 

  