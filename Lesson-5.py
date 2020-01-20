'''Задача 1
f = open('lesson-5.txt', 'w' encoding='utf-8')
print("Введите данные в файл: ")
while True:
    text = input()
    f.write(text + '\n')
    if text == "":
        break
f.close()
'''

'''Задача 2
with open('lesson5.txt', 'r', encoding='utf-8') as f:
    str_list = f.readlines()

print(f'Кол-во строк в этом файле {len(str_list)}')
for idx, el in enumerate(str_list):
    print(f'Строка {idx + 1}: {el.splitlines()}')
    print(f'Количество слов в {idx + 1} строке: {len(el.split())}')
'''

'''Задача 3
with open('lesson5.txt', 'r', encoding='utf-8') as f:
    str_list = f.readlines()

sum_zp = 0
for idx, el in enumerate(str_list):
    el = el.split(':')
    lastname = el[0]
    zp = int(el[1].splitlines()[0])
    if zp < 20000:
        print(f'{lastname} получает меньше 20000')
    sum_zp += zp
print(f'Средняя зарплата составляет {sum_zp / len(str_list)}')
'''

'''
Баталов:20000
Быков:15000   ################ Текстовый файл задача 3
Сидоров:100000
Смирнов:1000
'''

'''Задача 4
num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('lesson5.txt', 'r', encoding='utf-8') as f:
    read_f = f.readlines()

for el in read_f:
    numeral = el.split()[0]
    el = el.replace(numeral, num_dict[numeral])
    with open('lesson.res.txt', 'a', encoding='utf-8') as f:
        print(''.join(el.splitlines()), file=f)
'''

'''Задача 5
with open('lesson5.txt', 'w', encoding='utf-8') as f:
    f.write('12 2 1 20 24 65 26 23 28 33 30')

with open('lesson5.txt', 'r', encoding='utf-8') as f:
    read_file = f.readline().split()

summ = 0
for el in read_file:
    summ += int(el)
print(f'Сумма чисел в файле равна {summ}')
'''

'''Задача 6
with open('lesson5.txt', 'r', encoding='utf-8') as f:
    r_file = f.readlines()

arr = {}
for el in r_file:
    training = ''.join(el.split()[:1])[:-1]
    oth = el.split()[1:]
    summa = 0
    for el in oth:
        if el.isdigit():
            summa += int(el)
    arr.update({training: summa})

print(arr)
'''

'''
#текстовый файл lesson5 для задачи 6 
Информатика: 100 (л) 50 (пр) 20 (лаб).   ################ Текстовый файл задача 6
Физика: 30 (л) ​ —​ 10 (лаб)
Физкультура: ​ — 30 (пр) —
#
'''

'''Задача 7
with open("lesson5.txt", 'r', encoding='utf-8') as roll:
    dict1 = {}
    i = 0
    accum_profits = 0
    for line in roll:
        i += 1
        array = line.split(", ")
        profit = int(array[2]) - int(array[3])
        if profit >= 0:
            accum_profits = accum_profits + profit
        else:
            i -= 1
        dict1.update({array[0]: profit})
    average_profit = accum_profits // i
    enterprises = [dict1, {'average_profit': average_profit}]
    print(enterprises)

import json

with open("lesson5.json", 'w', encoding='utf-8') as jsonfile:
    json.dump(enterprises, jsonfile)
'''

'''
"Элком", ООО, 10000, 23000
"Сургутнефтегаз", ОАО, 5000, 300###################### Текстовый файл задача 7
"Яргео", ОАО, 300, 10000
'''