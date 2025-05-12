my_list = [1, 44, 0, 0, 32, 0, 1, 222, 0, 31]
zero_in_list = my_list.count(0)

without_zero = [num for num in my_list if num != 0]
all_zero = [zero for zero in my_list if zero == 0]

my_list_when_zero_on_the_and = without_zero + all_zero

pass
