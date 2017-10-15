"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""

def main():
    import random
    randoms_list = random.sample(xrange(100), 20)
    print "random list",randoms_list
    print res(randoms_list)


def res(lst):
    result =[]
    result.append(lst[0])
    result.append(lst[-1])
    return result

if __name__ == '__main__':
    main()
    
