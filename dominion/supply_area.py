
from dominion.pile import Pile
from dominion import dominion_data

class SupplyArea(object):

    TrashPile = Pile()
    CursePile = Pile()
    CopperPile = Pile()
    SilverPile = Pile()
    GoldPile = Pile()
    EstatePile = Pile()
    DuchyPile = Pile()
    ProvincePile = Pile()
    KingdomPiles = {}

    def __init__(self):
        self.TrashPile = Pile()
        self.CursePile = Pile()
        self.CopperPile = Pile()
        self.SilverPile = Pile()
        self.GoldPile = Pile()
        self.EstatePile = Pile()
        self.DuchyPile = Pile()
        self.ProvincePile = Pile()
        self.KingdomPiles = {}

    def allPiles(self):
        allPiles = self.KingdomPiles
        allPiles[dominion_data.cards['province']['name']] = self.ProvincePile
        allPiles[dominion_data.cards['duchy']['name']] = self.DuchyPile
        allPiles[dominion_data.cards['estate']['name']] = self.EstatePile
        allPiles[dominion_data.cards['copper']['name']] = self.CopperPile
        allPiles[dominion_data.cards['silver']['name']] = self.SilverPile
        allPiles[dominion_data.cards['gold']['name']] = self.GoldPile
        return allPiles