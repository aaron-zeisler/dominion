
class Card(object):

    Name = None
    Set = None
    Cost = None
    Type = None
    Effects = {}
    Image = None

    def __init__(self, name=None, set=None, cost=None, type=None, effects={}, image=None):
        self.Name = name
        self.Set = set
        self.Cost = cost
        self.Type = type
        self.Effects = effects
        self.Image = image

