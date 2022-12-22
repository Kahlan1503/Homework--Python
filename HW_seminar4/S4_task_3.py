# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# (Вывод тех элементов, которые были без повторов)
from collections import Counter
import random
max_num = int(input('Enter max number of massive: '))
mas_len = int(input('Enter massive Length: '))
i = 0
mass = [random.randint(1, max_num) for _ in range(mas_len)]
print(mass)
cow = Counter(mass)
print([i for i in cow if cow[i]==1])