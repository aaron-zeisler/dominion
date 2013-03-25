
class Card(object):

    Name = None
    Type = None
    Cost = None
    Effects = None
    ImageURL = None

    def __init__(self, name=None, type=None, cost=None, effects=None, imageUrl=None):
        self.Name = name
        self.Type = type
        self.Cost = cost
        self.Effects = effects
        self.ImageURL = imageUrl
