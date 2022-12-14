# Требуется посчитать сумму чётных чисел, 
# расположенных между числами 1 и N включительно
num = int(input('Enter number: '))
print(sum(i for i in range(2,num+1, 2)))