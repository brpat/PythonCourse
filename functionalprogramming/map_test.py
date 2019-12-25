from functools import reduce


def multiply2(item):
    return item * 2


# action, data(iterable)
print(list(map(multiply2, [1, 2, 3])))


# filter
def check_odd(item):
    return item % 2 != 0


# create new list of only odd values.
print(list(filter(check_odd, [1, 2, 3])))

# zip two iterables.
my_list = [1, 2, 3, 4, 5]
list2 = [7, 8, 9, 10, 11]
# combine both list
print(list(zip(my_list, list2)))


# reduce
# acc = 0, default is zero
def accumulator(acc, item):
    return acc + item


l1 = [1, 2, 3, 4, 5]
# noinspection PyTypeChecker
print(reduce(accumulator, l1, 0)) 
