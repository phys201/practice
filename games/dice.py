from numpy import random, sum


def roll_a_die(n):
    """this function returns a value 1-n"""
    return random.randint(n) + 1

def roll_two_dice(n):
    """this function returns sum of 2 randomly selected values 1-n"""
    return roll_a_die(n) + roll_a_die(n)


def roll_n(n, num_die):
    """ function to roll n die """
    print([roll_a_die(n) for num in range(1, num_die+1)])
    return sum([roll_a_die(n) for num in range(1, num_die+1)])