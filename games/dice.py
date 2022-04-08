from numpy import random


def roll_a_die(n):
    """this function returns a value 1-n"""
    return random.randint(n) + 1

def roll_two_dice(n):
    """this function returns sum of 2 randomly selected values 1-n"""
    return roll_a_die(n) + roll_a_die(n)


