
size = int(input('N: '))

list = []

for i in range(size):
    list.append([])
    for j in range(size):
        list[i].append(i * 10 + j)

print(list)
