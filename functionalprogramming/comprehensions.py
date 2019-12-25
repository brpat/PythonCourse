# list, set, dictionary
#param for param in iterable
my_list = [char for char in 'hello']
my_list2 = [num for num in range(0,100)]
my_list3 = [num for num in range(0,100) if num % 2 == 0]
print(my_list)
print(my_list2)
print(my_list3)


#set comprehensions.
my_list = {char for char in 'hello'}
print(my_list)

simple_dict = {
    'a': 1,
    'b': 2
}

#dictionary comprehensions.
my_dict = {key:val**2 for key,val in simple_dict.items()}
print(my_dict)


my_dict = {num:num*2 for num in [1,2,3]}
print(my_dict)