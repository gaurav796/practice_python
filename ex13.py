"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions. Make sure to ask the user to enter
the number of numbers in the sequence to generate. (The Fibonnaci seqence is a sequence of numbers
where the next number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, )
"""

import sys

def main():
    num = int(input("How many in your Fibonacci sequence? "))
    print fibonacci(num)


def fibonacci(num):
    if num <= 0:
        return []
    elif num == 1:
        return [1]
    else:
        fib = [1,1]
        for i in range(2,num):
            fib.append(fib[i-2] + fib[i-1])
            # print fib    
        return fib

if __name__ == '__main__':
    main()
