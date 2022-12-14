# Требуется найти наименьший натуральный делитель 
# целого числа N, отличный от 1
num = int(input('enter number: '))
for i in range(2,num + 1):
    if num % i == 0:
        print(f'НОД:  {i}')
        break
