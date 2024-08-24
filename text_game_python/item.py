from functions import *
import random

class Item:
    """Generic item class creation"""
    def __init__(self):
        self.name = ''
        self.description = ''
        self.quantity = 0
        self.type = ''

    
class Club(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.extra_damage = 10
        self.type = 'Weapon'



class Bandage(Item):
    """bandage that heals 10 hp"""
    def __init__(self):
        super().__init__()
        #healing set to 10
        self.name = 'Bandage'
        self.healing_amount = 10
        self.type = 'Consumable'
        self.description = (f"Clean bandages that heal {self.healing_amount} health")
    def use(self, player):
        #check to see if item is in inventory
        if self.quantity <= 0:
            print_slow(f"No {self.name} available")
            return
        else:
            print_slow(f"{self.name} used.")

        #heal up to healing amount and up to max health
        heal_count=0
        while player.health < player.max_health and heal_count < self.healing_amount:
            heal_count += 1
            player.health += 1

        #remove used bandage
        self.quantity -= 1
        if self.quantity < 1:
            player.remove_item(self)

        #print healing 
        if player.health == player.max_health:
            print_slow(f"{player.name} has full health.")

        else:
            print_slow(f"{player.name} has healed for {heal_count} health points")

class Magic_Mushroom(Item):
    """magic mushroom item, damages health and heals hunger"""
    def __init__(self):
        super().__init__()
        self.name = 'Magic Mushroom'
        self.description = 'Amanita Muscaria- consume with caution'
        self.hunger_amount = 20
        self.damage_amount = 10
        self.type = 'Consumable'
    
    def use(self, player):
        #check inventory for item
        if self.quantity <= 0:
            print_slow(f"No {self.name} available")
            return
        else:
            print_slow(f"{self.name} eaten.")

        #random event- nat 20, you regain max health and hunger; nat 1, instant death
        d20 = dice(20)
        if d20 == 1:
            print_slow(f"Dying alone wasn't enough. Instead you chose to go out the easy way, high on mushrooms..")
            print_slow(f"\033[0;31m{player.name} is dead.\033[0m\nGood luck next time.")
            exit()
        elif d20 == 20:
            print_slow(f"Super Mushroom Power-up! You now have max health and hunger.")
            player.hunger = player.max_hunger
            player.health = player.max_health

        #if not a 1 or 20, execute typical effect
        else:

            player.take_damage(self.damage_amount)

            player.gain_hunger(self.hunger_amount)

            #remove from inventory
            self.quantity -= 1
            if self.quantity < 1:
                player.remove_item(self)

            
 





#implement methods for adding and reducing health and hunger in player class. with message prompting for status updates (ie. stomach growling)