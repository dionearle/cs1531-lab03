'''
Number Guessing Game.

Guesses are made until all numbers are guessed.
The game reveals whether the closest unguessed number is higher or lower than each guess.
Numbers are distinct.
Typing 'q' quits the game.
'''

import random

MIN = 0
MAX = 10
NUM_VALUES = 3

def handle_guess(guess, values):

    # This function should return a duplicate list of values
    # with the guessed value removed if it was present.

    for i in range(len(values)):
        if (values[i] == int(guess)):
            del values[i]
            break

    return values

def find_closest(guess, values):
    # This function should return the closest value
    # to the guessed value.
    closest = values[0]
    distance = 100
    for i in range(len(values)):
        if (abs(values[i] - int(guess)) < distance):
            distance = abs(values[i] - int(guess))
            closest = values[i]

    return closest

def run_game(values):
    # While there are values to be guessed and the user hasn't
    # quit (with 'q'), the game should wait for the user to input
    # their guess and then reveal whether the closest number is
    # lower or higher.
    print(f'Numbers are between {MIN} and {MAX} inclusive. There are {len(values)} values left.')
    guess = input('Guess: ')
    # Your code goes here.
    while (guess != 'q' and len(values) != 0):
        found = 0
        for i in range(len(values)):
            if (values[i] == int(guess)):
                handle_guess(guess, values)
                print(f'You found {guess}! It was in the list.')
                found = 1
                break
        if (found == 0):
            closest = find_closest(guess, values)
            if (closest > int(guess)):
                print(f'The closest to {guess} is higher.')
            else:
                print(f'The closest to {guess} is lower.')

        if (len(values) == 0):
            print('Congratulations! You won!')
        else:
            print(f'There are {len(values)} values left.')
            guess = input('Guess: ')

    print('Thanks for playing! See you soon.')

if __name__ == '__main__':
    values = sorted(random.sample(range(MIN, MAX+1), NUM_VALUES))
    run_game(values)
