"""
Ask the user for a string and print out whether 
this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""


def main():
    print('Please enter a string')
    string = raw_input()
    string = string.strip().lower()
    return is_palindrome(string)


def is_palindrome(string):
    rev_str = string[::-1]
    if string == rev_str:
        print('given string is a palindrome')
    else:
        print('not palindrome')

if __name__ == '__main__':
    main()

