# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N
from itertools import accumulate
n = int(input('enter number; '))
print(list(accumulate(range(1,n +1), lambda x, y: x* y)))