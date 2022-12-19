# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции

import random
num = int(input('Enter max number of massive: '))
dl = int(input('Enter massive Length: '))
mass = [random.randint(0, num)for _ in range(dl)]
print(f'massive {mass} ')
res = sum([mass[i]for i in range(1,len(mass),2)])
print(res)