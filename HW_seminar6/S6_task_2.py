# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

seq = [12,'sadf',5643]

print( list(filter(lambda x: isinstance(x,str) , seq)), list(filter(lambda x: not isinstance(x,str) , seq)) )