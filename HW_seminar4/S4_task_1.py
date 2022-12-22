# Вычислить число Pi c заданной точностью d, не используя ф. round()
import math
d = float(input('Задайте точность '))
print(float(str(int(math.pi))+ '.' + str(int(math.pi % 1// d))))