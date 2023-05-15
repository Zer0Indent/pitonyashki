
def frame(size):

    if size == 1:
        return '*'
    elif size == 2:
        return '**\n**'
    else:
        type1 = '*' * size
        type2 = ('*' + ' ' * (size-2) + '*' + '\n') 
        return f'{type1}\n{type2 * (size-2)}{type1}'


for i in range(1, 11):
    print(i)
    print(frame(i))


#print(frame(5))