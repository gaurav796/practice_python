'''
Write a program (function!) that takes a list and returns a new list that contains 
all the elements of the first list minus all the duplicates.
Extras:
- Write two different functions to do this - one using a loop and constructing a list,
  and another using sets.
- Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''

import random
randoms_first = random.sample(xrange(100), 10)
randoms_second = random.sample(xrange(100), 20)

def main():
    
    print('First list of 10 numbers')
    print(randoms_first)
    print('second list of 20 numbers')
    print(randoms_second)
    result_list = []

    for i in randoms_first:
        if i in randoms_second:
            result_list.append(i)
    if len(result_list) > 0:
        print('list of common numbers in above 2 lists')
        # list(set(source_list)) will remove duplicates in source_list.
        # A set can't have duplicates.
        # result_list = [2, 2, 3, 3, 4, 5, 6]
        # print(result_list)
        print (list(set(result_list)))

if __name__ == '__main__':
    main()
        
