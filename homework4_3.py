import random

random_list = random.randint(3, 10)
my_list = [random.randint(3, 10) for num in range(random_list)]

new_list = [my_list[0], my_list[2], my_list[-2]]


pass
