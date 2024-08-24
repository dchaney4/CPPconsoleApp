from functions import *
from player import *

class Bear:
    """create bear class"""
    def __init__(self):
        self.name = 'Bear'
        self.health = 50
        self.damage = 20

    def attack(self, target):
        self.target = target
        print_fast(f"The massive beast lunges at you, ready to tear you from limb to limb.")
        attack_die = dice(20)
        if attack_die > 8:
            target.take_damage(self.damage)
            

        elif attack_die == 20:
            print_fast(f"CRITICAL HIT")
            critical_hit = self.damage * 1.5
            target.take_damage(critical_hit)
            

        else:
            print_fast(f"The bear swings wildly and misses wildly.")