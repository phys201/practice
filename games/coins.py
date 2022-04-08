from numpy import random


def flip_a_coin():
    """this function flips a coin"""
    print("Tails never fails!")
    return random.choice(["heads", "tails"])
