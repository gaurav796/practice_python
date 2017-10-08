#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3
"""
Ex 2:
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
Extras:
(1) If the number is a multiple of 4, print out a different message.
(2) Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""


def main():
    number = raw_input("please provide a number: ")
    number = int(number)
    if number % 2 == 0:
        if number % 4 == 0:
            print('Your number is a multiple of 4')
        else:
            print ('Your number is Even')
    else:
        print ('Your number is Odd')


int1 = int(raw_input("Please enter an integer numerator: "))
int2 = int(raw_input("Please enter an integer denominator: "))

if int2 == 0:
    print('denominator can not be 0')
    exit()
else:
    if int1 % int2 == 0:
        print('divides perfectly')
    else:
        print('does not divide perfectly')

if __name__ == '__main__':
    main() 

