my_str = input('Введите строку')
def negative (i):
	if (i > 0):
		return -i

i = 1
new_str = ''

while (i <= len(my_str)):
	new_str += my_str[negative(i)]
	i += 1	

print(new_str)


# второй вариант без функции negative

while (len(my_str) >= i):
  new_str += my_str[len(my_str) - i] 
  i += 1

print(new_str)

	