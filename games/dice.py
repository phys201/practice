from numpy import random, sum


def roll_a_die(n):
    """this function returns a value 1-n, add 1 so the number start from 1"""
    return random.randint(n) + 1

def not_even_die():
     """this function returns an uneven die"""
     return np.pop([1,2,1,1,1,1,4,5,6,3])

def roll_uneven_die():
    return not_even_die()
