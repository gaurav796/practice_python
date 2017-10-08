#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3
"""

Create a program that asks the user for a number and then prints out a list of 
all the divisors of that number. (If you don't know what a divisor is, it is a number 
that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

"""


def main():
    print('Please enter a number')
    x = raw_input()
    x = abs(int(x))
    divisors = get_divisors(x)
    if len(divisors) == 0:
        print('no divisor except 1 and number itself')
    else:
        print divisors


def get_divisors(n):
    divs = []
    for i in range(2, n):
        if n % i == 0:
            divs.append(i)
    return divs


if __name__ == '__main__':
    main()

