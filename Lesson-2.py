'''Задача 1
def checkType(a_list):
    for element in a_list:
        if isinstance(element, int):
            print("It an Integer")
        if isinstance(element, str):
            print("It an string")
        if isinstance(element, float):
            print("It an floating number")

a = [1, 2, 3,4.55,2]
a.append("hello") 
checkType(a)
'''


'''Задача 2
from random import randint
a = list(input())
print(a)
 
for i in range(0,len(a)-1,2):
    a[i], a[i+1] = a[i+1], a[i]
 
print(a)
'''

'''Задача 3
month = int(input('Напишите месяц: '))
seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}
for key in seasons.keys():
    if month in seasons[key]:
        print("Это " + key)
'''



'''Задача 4
text = input("Ожидаю ввод: ")
i=0
import re
for x in re.split(r'\s+', text):
    i=i+1
    print(i,x[0:10])
'''




'''Задача 5
def rz(a, value):
    l, r = -1, len(a)
    while l + 1 < r:
        mid = (l + r) // 2
        if value <= a[mid]:
            l = mid
        else:
            r = mid
    return r

def insort_reversed_right(a, value):
    a.insert(rz(a, value), value)
my_list = [7, 5, 3, 3, 2]
print(my_list)
a=int(input("Введите значение "))
insort_reversed_right(my_list, a)
print(my_list)
while a !=127:
    a=int(input("Введите значение "))
    insort_reversed_right(my_list, a)
    print(my_list)
'''