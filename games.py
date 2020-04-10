from numpy import random


def flip_a_coin():
    """this function flips a coin"""
    return random.choice(['heads', 'tails'])


def pick_a_card():
    """this function picks a card """
    value = random.randint(1, 14)
    suit = random.randint(4)
    return (value, suit)


def roll_a_die():
    """this function returns a value 1-6"""
    return random.randint(6) + 1

  
def roll_two_dice():
    """this function returns sum of 2 randomly selected values 1-6"""
    return roll_a_die() + roll_a_die()

  
def roll_three_dice():
    """this function returns sum of 3 randomly selected values 1-6"""
    return roll_a_die() + roll_a_die() + roll_a_die()

