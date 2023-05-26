def dec_to_oct(dec):

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

dec_number = int(input())

print(dec_to_oct(dec_number))





