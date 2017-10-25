'''
Write a password generator in Python.
Be creative with how you generate passwords - strong passwords have a mix of
lowercase letters, uppercase letters, numbers, and symbols. The passwords should be
random, generating a new password every time the user asks for
a new password. Include your run-time code in a main method.

Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''
import random, string
from string import punctuation


def main():
    length= int(raw_input('Please enter length: '))
    password = generate_password(length)
    print password


def generate_password(length):
    letters= string.letters
    print letters
    digits = string.digits
    print digits
    special_char = string.punctuation
    print punctuation
    chars = letters + digits + punctuation
    print string.printable
    password = ''

    for i in range(0,length):
        password += str(random.choice(chars))
        #password += str(random.choice(string.printable))
    return password    

if __name__ == '__main__':
    main()
    
