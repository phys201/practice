from numpy import random


def flip_a_coin():
    """this function flips a coin"""
    print("Come on tails!")
    return random.choice(['heads', 'tails'])

def flip_two_coins():
    """this function flips a coin"""
    print("Come on tails!")
    return (random.choice(['heads', 'tails']),random.choice(['heads','tails'])

