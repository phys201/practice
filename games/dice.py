from numpy import random


def roll_a_die():
    """this function returns a value 1-6"""
    return random.randint(6) + 1


def roll_two_dice():
    """this function returns sum of 2 randomly selected values 1-6"""
    return roll_a_die() + roll_a_die()


def roll_three_dice():
    """this function returns sum of 3 randomly selected values 1-6"""
    return roll_a_die() + roll_a_die() + roll_a_die()

def roll_d20():
    """this function returns a value 1-20"""
    return random.randint(6) + 1
