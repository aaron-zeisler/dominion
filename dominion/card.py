
class Card(object):

    Name = None
    Cost = None
    VictoryPoints = None

    def __init__(self, name=None, cost=None, victoryPoints=None):
        self.Name = name
        self.Cost = cost
        self.VictoryPoints = victoryPoints
