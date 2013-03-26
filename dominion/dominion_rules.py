
class GAME_SETUP:
    COPPER_CARDS = 60
    SILVER_CARDS = 40
    GOLD_CARDS = 30
    VICTORY_CARDS_2_PLAYERS = 8
    VICTORY_CARDS_3_OR_4_PLAYERS = 12
    CURSE_CARDS = 30
    KINGDOM_CARDS = 10


class FIRST_DECK:
    COPPER_CARDS = 7
    ESTATE_CARDS = 3

HAND_SIZE = 5


def getGameSetupVictoryCardCount(numberOfPlayers):
    if numberOfPlayers == 2:
        return GAME_SETUP.VICTORY_CARDS_2_PLAYERS
    else:
        return GAME_SETUP.VICTORY_CARDS_3_OR_4_PLAYERS