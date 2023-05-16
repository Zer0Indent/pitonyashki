def combo(string):
    x = string[0]
    y = string[1] 
    z = string[2]  
    return f'{x}{y}{z}, {x}{z}{y}, {y}{x}{z}, {y}{z}{x}, {z}{x}{y}, {z}{y}{x}'

number = input('Введите число')
print(combo(number))






