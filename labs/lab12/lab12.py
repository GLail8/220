"""
Garrett Lail
lab12.py
I certify this lab is my own work

"""

def find_and_remove_first(list, value):
    i = 0
    while i < len(list):
        if list[i] == value:
            list.insert(i, 'Garrett')
            list.remove(list[i+1])
            i += 1
        else:
            i += 1
    print(list)

from algorithms import is_in_linear, read_data

def good_input():
    list_range = list(range(1,11))
    user_input = eval(input('input a number from 1 to 10: '))
    while user_input not in list_range:
        if user_input > 10:
            print('that number is too big')
            user_input = eval(input('input a number from 1 to 10: '))
        if user_input < 1:
            print('that number is too small')
            user_input = eval(input('input a number from 1 to 10: '))
        if type(user_input) == float:
            print('that is a float, enter an int')
            user_input = eval(input('input a number from 1 to 10: '))
    print(user_input)

def num_digits():
    user_input = eval(input('input a positive integer: '))
    while user_input > 0:
        digits = 0
        while user_input > 0:
            user_input //= 10
            digits += 1
        print(digits)
        user_input = eval(input('input a positive integer: '))

from random import randint

def hi_lo_game():
    rand = randint(1, 100)
    guesses = 1
    guessed = 6
    guess = eval(input('Guess a number from 1 to 100: '))
    while guessed > 0 and guess != rand:
        if guess > rand:
            print('too high')
            guess = eval(input('Guess a number from 1 to 100: '))
            guessed -= 1
            guesses += 1
        if guess < rand:
            print('too low')
            guess = eval(input('Guess a number from 1 to 100: '))
            guessed -= 1
            guesses += 1
        if guess == rand:
            print('correct')
    if guessed == 0:
        print('Sorry, you lose. The number was {}.'.format(rand))
    if guess == rand:
        print('You win in {} guesses!'.format(guesses))

if __name__ == '__main__':
    find_and_remove_first(['George', 'Greg', 'Gary', 'Grant', 'Gabriel', 'Graham'], 'Greg')
    is_in_linear('5', read_data('data_sorted.txt'))
    is_in_linear('6', read_data('data_sorted.txt'))
    good_input()
    num_digits()
    hi_lo_game()

