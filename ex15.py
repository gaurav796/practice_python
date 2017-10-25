'''
Write a program (using functions!) that asks the user for a long string containing
multiple words. Print back to the user the same string, except with the words in
backwards order. For example, say I type the string:

My name is Michele
Then I would see the string:
Michele is name My

'''

def main():
    sentence = raw_input('please enter your name ')
    print reverse(sentence)


def reverse(str):
    str_split = str.split() #split on whitespace
    str_split.reverse()
    return ' '.join(str_split)
 
if __name__ == '__main__':
    main()
    
