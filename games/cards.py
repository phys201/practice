from numpy import random


def pick_a_card():
    """this function picks a card """
    value = random.randint(1, 14)
    if value == 11:
        value = 'J'
    else if value == 12:
        value = 'Q'
    else if value == 13:
        value = 'K'
    suit = random.randint(4)
    suit = ['clubs', 'diamonds', 'hearts', 'spades'][suit]
    return (value, suit)
