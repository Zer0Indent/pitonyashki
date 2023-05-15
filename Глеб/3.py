def from2to16(number):
    number = str(number)
    length = len(number)
    number = '0' * (length // 4 * 4 + (0 if length % 4 == 0 else 1) * 4 - length) + number
    
    result = ''
    end = len(number) // 4
    for i in range(end):
        fragment = number[i*4:i*4+4]
        result = result + hexSymbol(fragment)
    return result

def hexSymbol(fragment):
    symbols = '0123456789ABCDEF'
    index = 0
    index = index + 8 * int(fragment[0])
    index = index + 4 * int(fragment[1])
    index = index + 2 * int(fragment[2])
    index = index + 1 * int(fragment[3])
    return symbols[index]



#assert from2to16(10101101001) == 
print(from2to16(10101101001))