from numpy import random


def flip_a_coin():
    """this function flips a coin"""
    print("Come on tails!")
    return random.choice(['heads', 'tails'])