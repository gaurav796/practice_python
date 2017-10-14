''' 
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

Extras:
Keep the game going until the user types exit
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

import random
import sys


def main():
    """DocString strats now --forms a user input
    """
    num_guess = 0
    while 1:
        user_input = raw_input('Please guess any number between 1 and 9 or type "exit" to quit:')
        if user_input == 'exit':
            print 'you guessed {} times.' .format(num_guess)
            sys.exit()
        num_guess += 1
        guess = int(user_input)
        randon_num = random.randint(1, 9)
        print 'random integer', randon_num
        if guess == randon_num:
            print 'you got it right'
        elif guess < randon_num:
            print 'you guessed a smaller number'
        else:
            print 'you guesses a larger number'

if __name__ == '__main__':
    main() 

