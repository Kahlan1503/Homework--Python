# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.
def Ten2two(num):
    rez = []
    while True:
        if num/2 == 0:
            break
        ost = num%2
        if ost == 0:
            rez.append('0')
        else:
            rez.append('1')
        num //=2
    return "".join(rez[::-1])

print(Ten2two(int(input('Enternumber to convert: '))))