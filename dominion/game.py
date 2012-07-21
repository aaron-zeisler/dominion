
from dominion.supply_area import SupplyArea as SupplyAreaClass
from dominion.card import Card

class Game(object):

    Players = []
    SupplyArea = SupplyAreaClass()

    def __init__(self):
        self.Players = []
        self.SupplyArea = SupplyAreaClass()

    def addPlayer(self, player):
        self.Players.append(player)

    def initialize(self):
        #TODO:
        # 1) Add Copper, Silver, and Gold to the SupplyArea
        # 2) Add Estates, Duchies, and Provinces to the SupplyArea
        # 3) Add Curses to the SupplyArea
        # 4) Add Kingdom Cards to the SupplyArea
        # 5) Deal Copper and Estate cards to each Player's DrawPile
        # 6) Shuffle each Player's DrawPile
        # 7) Have each Player draw 5 cards from their DrawPile into the Hand
        pass
