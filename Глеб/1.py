FIO = '!Иванов А. С.'

result = ''

i = 0
lenFIO = len(FIO)

while i < lenFIO:
    bukva = FIO[i]
    i = i + 1
    if bukva != ' ' and bukva != '.' and bukva != '!':
        result = result + bukva
        print(bukva, result)

print(result)