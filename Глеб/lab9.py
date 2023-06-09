
#def BASE_to_DEC(value, base):
#def DEC_to_BASE(value, base):
#def conv(value, from_base, to_base):

# 10 >> 10 - само число
# 2 >> 10, 8 >> 10, 16 >> 10 - BASE_to_DEC
# 10 >> 2, ... - DEC_to_BASE
# 16 >> 2 - BASE_to_DEC, DEC_to_BASE


def BIN_to_DEC(binary):
	
	result = 0
	length = len(binary)
	
	for i in range(length):
		result += int(binary[length - 1 - i]) * 2 ** i
	
	return result

def from2to16(number):
    number = str(number)
    length = len(number)

    number = '0' * (length // 4 * 4 + (0 if length % 4 == 0 else 1) * 4 - length)
    number += number

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


print(from2to16(1010010001011))