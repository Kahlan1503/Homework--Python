# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def SM(num,dell = 2):
    for i in range(dell,num):
        if num%i ==0:
            return[i] + SM(int(num/i), dell = i)
    return [num]
print(SM(int(input('Enter your number: '))))