my_list = [1, 5, 3, 6, 11, 0, 2, 3]
new_list = []

if my_list:
    for inx, num in enumerate(my_list):
        if inx % 2 == 0:
            new_list.append(num)
    result = sum(new_list) * my_list[-1]


pass
