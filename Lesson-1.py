
'''Задача1
name = input("Привет,не могли бы вы представиться ? \n")
print("Приятно познакомиться, " + name.title() + "\n")
print("Сколько вам лет ? ")
engAge = int(input())
city = input("Из какого вы города?  ")
if city == "Екатеринбург":
    print("Круто,я тоже")
else :
    print("Классно,а я из Екатеринбурга")
print("Приятно познакомиться, " + name.title() + "!\nВаш возраст " + str(engAge) + " лет(год)" + " и вы из " + city.title())
'''


'''Задача2
sec = int(input("Введите количество секунд  "))
h = sec // 3600
m = (sec-h*3600) // 60 
s = sec % 60
print(h,'час',m,'мин',s,'сек')
'''


'''Задача3
n = (input("Введите значение n  "))
n1=n
n2=n+n
n3=n+n+n
print(int(n1)+int(n2)+int(n3))
'''

'''Задача4
a = int(input("Введите число"))
max = 0
while a > 0:
    end=a%10
    if end > max:
        max = end
    a = a//10
print(max)
'''


'''Задача5
v = int(input("Значение выручки вашей фирмы?"))
i = int(input("Издержки вашей фирмы?"))
rez = input("С каким финансовым результатом работает ваша фирма? ")
print("Вы сказали что ваша фирма работает в " + rez.title() + "\n")
if rez == "прибыль" and v>i:
    p=v-i
    r=p/v
    print("Рентабельность вашей фирмы" + str(r))
    one = int(input("Сколько сотрудников в вашей фирме?"))
    oneprib=p/one
    print("Прибыль составляет " + str(oneprib) + "   на количество сотрудников = " + str(one))
if rez == "убыток" and v<i:
    print("Ваша фирма находится в убытке")
if rez == "прибыль" and v<=i:
    print("Извините,вы сказали что работаете в прибыль, но это не так")
'''


'''Задача6
a = int(input("Введите значение a "))
while a<=0:
    a = int(input("Введите положительное значение a "))
b = int(input("Введите значение b "))
while b<=0:
    b = int(input("Введите положительное значение b "))
while b<a:
    print("Значение b не должно быть меньше a")
    a = int(input("Введите положительное значение a "))
    b = int(input("Введите положительное значение b "))
day = 1
while b - a > 0:
    a = a + (a * 0.1)
    day += 1
    print(str(day) + "-й день :" +  str(round(a,2)))
'''