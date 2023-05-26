def bubble_sort(arr):
    border = len(arr) - 1

    while border >= 1:
        itr = 0
        while itr < border:
            if arr[itr] > arr[itr + 1]:
                temp = arr[itr]
                arr[itr] = arr[itr + 1]
                arr[itr + 1] = temp
            itr += 1

        border -= 1
    return arr


arr_size = int(input("Введите размер массива: "))
my_arr = []

for item in range(0, arr_size):
    next_item = int(input("Введите число: "))
    my_arr.append(next_item)

print(bubble_sort(my_arr))