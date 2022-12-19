# Задайте список из вещественных чисел. 
# Напишите программу, которая 
# найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
import random
#Задаем длину массива
leng = int(input('Enter massive length: '))

#Заполняе массив
mass =[random.random()*10 for _ in range(leng)]
print(mass)
#Считаем
rez = max(i%1 for i in mass) - (min(i%1 for i in mass))
print(rez)