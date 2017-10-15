"""
This week exercise is going to be revisiting an old exercise (see Exercise 5),
except require the solution in a different way.
Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common
between the lists (without duplicates). Make sure your program works on two lists of different sizes.
Write this in one line of Python. (Hint: Remember list comprehensions from Exercise 7).
Extra: Randomly generate two lists to test this
"""
import random

def main():
    randoms_first = random.sample(xrange(100), 10)
    randoms_second = random.sample(xrange(100), 20)

    print('First list of 10 numbers')
    print(randoms_first)
    print('second list of 20 numbers')
    print(randoms_second)
    
    result = [i for i in randoms_first if i in randoms_second]
    print result

if __name__ == '__main__':
    main()
