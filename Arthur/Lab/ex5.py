def is_even(usr_list):
    new_list = []
    for item in usr_list:
        if item % 2 == 0:
            new_list.append(item)
    return new_list


my_list = list(range(10))

print(is_even(my_list))