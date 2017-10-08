import random
randoms_first = random.sample(xrange(100), 10)
randoms_second = random.sample(xrange(100), 20)

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
