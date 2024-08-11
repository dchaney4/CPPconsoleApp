from functions import *
from item import *
from player import *
from threat import *


class Location:
    def __init__(self, description):
        self.description = description
        self.close_item = []
        self.close_threat = []

    def add_items(self, item):
        self.close_item.append(item)

    def add_threat(self, threat):
        self.close_threat.append(threat)




