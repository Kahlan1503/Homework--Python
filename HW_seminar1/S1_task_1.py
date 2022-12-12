#Получаем число дня недели
day = int(input('Enter the day of week number '))
#цикл для проверки выходной день или будний день
if 0<day<6:
    print('Будний день ')
elif 8>day>5:
    print('Выходной ')
else:
    print('INVALID DATA')

