from numpy import random

def pick_a_card():
    """this function picks a card """
    value = random.randint(1, 14)
    suit = random.randint(4)
    suit = ['Annikas suit test', 'diamonds', 'hearts', 'spades'][suit]
    return (value, suit)
