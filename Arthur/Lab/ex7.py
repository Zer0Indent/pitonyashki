def arr_diagonal(arr):
    itr = 0
    while arr_size > itr:
        print('  ' * itr, arr[itr][itr])
        itr += 1

arr_size = int(input("Введите размер массива: "))
my_arr = list(range(arr_size))

for k in range(arr_size):
    my_arr[k] = list(range(arr_size))

for i in range(arr_size):
    for j in range(arr_size):
        iterator = 10
        my_arr[i][j] = my_arr[i][j] * iterator + i


print(my_arr)

# for item in range(arr_size):
#     next_item = int(input("Введите число: "))
#     my_arr.append(next_item)
#
#
# for i in range(arr_size):
#    s = input("Введите числа: ")
#    s = s.split()
#    for j in range(arr_size):
#        my_arr[i][j] = int(s[j])