from numpy import random


def flip_a_coin():
    return random.choice(['heads', 'tails'])


def pick_a_card():
    value = random.randint(1, 14)
    suit = random.randint(4)
    return (value, suit)


def roll_a_die():
    return random.randint(6)

def roll_two_dice()
    return roll_a_die() + roll_a_die()