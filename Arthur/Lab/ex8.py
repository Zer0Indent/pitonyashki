import random


def fill_arr(arr_str, arr_col):
    my_arr = list(range(N))
    for index in range(arr_str):
        my_arr[index] = list(range(arr_col))

    for index in range(arr_str):
        res = random.sample(range(100), arr_col)
        for index2 in range(arr_col):
            my_arr[index][index2] = res[index2]

    return my_arr
# todo сделать выходной массив


N = int(input("Введите кол-во строк 1 массива: "))
M = int(input("Введите кол-во столбцов 1 массива: "))


arr_1 = fill_arr(N, M)
arr_2 = fill_arr(N, M)


for itr in range(N):
    for itr2 in range(M):
        print(arr_1[itr][itr2] * arr_2[itr][itr2], end=" ")
    print('\n')


# for item in range(N):
#     next_item = int(input("Введите число: "))
#     my_arr.append(next_item)


# for i in range(N):
#     s = input("Введите числа: ")
#     s = s.split()
#     for j in range(M):
#         my_arr[i][j] = int(s[j])


# for item in my_arr:
#   print(item)

