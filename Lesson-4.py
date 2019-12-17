'''Задача 1
from sys import argv

script_name, first_param, second_param, third_param = argv

print("Имя скрипта: ", script_name)
print("Количество отработанных часов: ", first_param)
print("Cуммf оплаты труда за 1 чаc: ", second_param)
print("Размер премии: ", third_param)
def simple_calc():  # Расчёты зарплаты
    x = int(first_param)
    y = int(second_param)
    c = int(third_param)
    pay = x * y
    return pay + c
print(f'Размер заработной платы составил: {simple_calc() }')
'''


'''Задача 2
a = [1,2,5,2,8,12,5,2,90,321,54,2,1,4,3]
b = []
for i in range(len(a)-1):
    n = int(a[i])
    i += 1
    m = int(a[i])
    if m > n:
        n = m
        b.append(m)
print(b)
'''

'''Задача 3
p = [q for q in range(20, 241) if not q%21 or not q%22]
print(p)
'''

'''Задача 4
lst = [1, 2, 4, 5, 6, 2, 5, 2]
used = set()
unique = [x for x in lst if x not in used and (used.add(x) or True)]
from collections import Counter
counter = Counter(lst)
unique = list(counter)
single = [x for x,n in counter.items() if n==1]
print(single)
'''

'''Задача 5
p = [q for q in range(100, 1000) if not q%2]
summa=0
for el in p:
    summa += el
print(summa)
'''

'''Задача 6
import itertools

for i in itertools.count(1):
    print (i)
    if i > 50:
        break
        
#Вторая часть      
import itertools
list = [2, 4, 5]
for i in itertools.cycle(list):
    print (i)
'''

'''Задача 7
import math
nubmer=int(input())
i=0
def fibo_gen(x):
    a = 1
    for i in range(1, x+1):
        a *= i
        yield a
for el in fibo_gen(nubmer):
    i=i+1
    el=str(el)
    print(el[:15])
'''

