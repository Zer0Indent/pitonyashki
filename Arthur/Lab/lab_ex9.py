def BIN_to_DEC(binary):
    binary = int(binary)
    dec_num = 0
    pow_of_num = 0

    while binary != 0: 
        dec_num += (binary % 10) * 2 ** pow_of_num
        pow_of_num += 1
        binary //= 10

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
			
			#hex_num.append('ABCDEF'[dec_num - 10] if dec_num>= 10 else str(dec_num))

			if dec_num == 10:
				hex_num.append('A')
			elif dec_num == 11:
				hex_num.append('B')
			elif dec_num == 12:
				hex_num.append('C')
			elif dec_num == 13:
				hex_num.append('D')
			elif dec_num == 14:
				hex_num.append('E')
			elif dec_num == 15:
				hex_num.append('F')
			else:
				hex_num.append(str(dec_num))

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

def DEC_to_Hex(decimal):
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


#dec_number = int(input())
#print(dec_to_oct(dec_number))



#print(BIN_to_DEC('101001'))
#print(BIN_to_HEX(1010010001011))
#print(BIN_to_OCT(1000))
#print(DEC_to_BIN(1000))