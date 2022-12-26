# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = 6782

print( sum(int(i) for i in str(number) if i.isdigit()) )