my_list = [1, 2, 3, 5, 88]
my_list = [my_list[-1]] + [my_list[:-1]]
print(my_list)

my_list2 = ["apple", "banana", "lemon", "orange", "milk"]
my_list2.insert(0, my_list2.pop())
print(my_list2)


pass
