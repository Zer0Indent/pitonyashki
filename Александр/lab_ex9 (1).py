
def BIN_to_DEC(binary):

    binary = binary
    dec_num = 0
    pow_of_num = 0

    while binary != 0: 
        dec_num += (binary % 10) * 2 ** pow_of_num
        pow_of_num += 1
        binary //= 10

    return dec_num

def OCT_to_DEC(oct):
    
    dec = 0
    i = 0

    while oct > 0: #500 > 0
        dec += oct % 10 * (8 ** i)   #500 % 10  
        oct //= 10
        i += 1
    return dec

def HEX_to_DEC(hexadecimal):

    hexadecimalNum = str(hexadecimal)
    dec_num = 0  
    array = []

    for st_item in hexadecimalNum[::-1]:  # 'FFF'
        if st_item == 'A':
            array.append(10)
        elif st_item == 'B':
            array.append(11)
        elif st_item == 'C':
            array.append(12)
        elif st_item == 'D':
            array.append(13)
        elif st_item == 'E':
            array.append(14)
        elif st_item == 'F':
            array.append(15) 
        else:      
            array.append(int(st_item))

    for a_item in range(0, len(array)):
        dec_num = dec_num + array[a_item] * 16 ** a_item

    return dec_num

def BIN_to_HEX(binary):

    hex_num = []
    dec_num = 0
    pow_of_num = 0
    counter = 0

    while binary != 0: 
        dec_num += (binary % 10) * 2 ** pow_of_num
        pow_of_num += 1
        counter += 1
        binary //= 10

        if counter == 4:
            
            hex_num.append('ABCDEF'[dec_num - 10] if dec_num >= 10 else str(dec_num))
            counter = 0
            pow_of_num = 0
            dec_num = 0

    hex_num.append(str(dec_num))
    hex_num.reverse()
    my_str = ''

    for item in hex_num:
        my_str += item  

    return my_str

def BIN_to_OCT(binary):

    oct_num = []
    dec_num = 0
    pow_of_num = 0
    counter = 0

    while binary != 0:
        dec_num += (binary % 10) * 2 ** pow_of_num
        pow_of_num += 1
        counter += 1
        binary //= 10

        if counter == 3:

            oct_num.append(str(dec_num))
            counter = 0
            pow_of_num = 0
            dec_num = 0

    oct_num.append(str(dec_num))
    oct_num.reverse()
    my_str = ''

    for item in oct_num:
        my_str += item

    return my_str

def DEC_to_BIN(decimal):

    rem = 0
    binary = []
    div = decimal

    while div // 2 != 0:
        rem = div % 2
        binary.append(str(rem))
        div //= 2

    binary.append(str(div % 2))
    binary.reverse()

    my_str = ''

    for item in binary:
        my_str += item

    return my_str

def DEC_to_HEX(decimal):

    rem = 0
    hexadecimal = []
    div = decimal

    while div // 16 != 0:
        rem = div % 16
        hexadecimal.append('ABCDEF'[rem - 10] if rem >= 10 else str(rem))
        div //= 16

    hexadecimal.append('ABCDEF'[(div % 16) - 10] if div % 16 >= 10 else str(div % 16))
    hexadecimal.reverse()

    my_str = ''

    for item in hexadecimal:
        my_str += item

    return my_str

def DEC_to_OCT(dec):

    dec_to_oct = dec
    rem = 0
    arr = []

    while dec_to_oct != 0:
        rem = dec_to_oct % 8
        dec_to_oct = dec_to_oct // 8
        arr.append(rem)
        
    arr.reverse()
    string = ""

    for i in arr:
        string += str(i)

    return string

#def OCT_to_DEC(octal):
    #octal_num = octal
    #dec_num = 0
    #pow_of_num = 0
    #while octal_num != 0:
        #dec_num += (octal_num % 10) * 8 ** pow_of_num
        #pow_of_num += 1
        #octal_num //= 10
    #return dec_num

# def conv(value, from_base, to_base)
# def DEC_to_BASE(value, base):

def BASE_to_DEC(value, base): #base 2, 8, 16 

    if base == 2:
        return BIN_to_DEC(value)
    elif base == 8:
        return OCT_to_DEC(value)
    elif base == 16:
        return HEX_to_DEC(value)
    else:
        return value

def DEC_to_BASE(value, base): 

    if base == 2:
        return DEC_to_BIN(value)
    elif base == 8:
        return DEC_to_OCT(value)
    elif base == 16:
        return DEC_to_HEX(value)
    else:
        return value

def conv(value, from_base, to_base): # 1111, 2, 16

    val = DEC_to_BASE(BASE_to_DEC(value, from_base), to_base)
    return val


print(conv(16526376347664254576, 8, 16))