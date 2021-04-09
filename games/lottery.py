from numpy import random


def generate_ticket():
    """this function generates a lottery ticket with 8 numbers"""
    values = random.randint(1, 100, 8)
    return list(values)

def did_I_win(lottery_number):
    """this function tells the prize for the lottery"""
    win_number = random.randint(1,100,8)
    win_number_count = dict((i,win_number.count(i)) for i in win_number)
    if list(win_number) == lottery_number :
        print("You've won!")
    elif list(win_number)