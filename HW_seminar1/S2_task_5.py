#Напишите программу, которая принимает на вход координаты двух точек 
#и находит расстояние между ними в 2D пространстве.

def coord_in(x):
    xy = ['X','Y']
    a = []
    for i in range(x):
        num = int(input(f'Введите значение по {xy[i]} '))
        a.append(num)
    return a

def calc(a,b):
    lenth = ((b[0]-a[0])**2 + (b[1]- a[1])**2)**0.5
    return lenth

print('Введите координаты точки А ')
poA = coord_in(2)
print('Введите координаты точки В ')
poB = coord_in(2)
print(f"Длина отрезка = {format(calc(poA, poB), '.2f')}")