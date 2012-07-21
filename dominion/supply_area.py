
from dominion.pile import Pile

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
