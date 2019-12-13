'''Задача 1
def my_fun():
    a = int(input("Введите значение первого числа " ))
    while a == 0 :
        a = int(input("Введите значение первого числа,делить на ноль нельзя " ))
    b = int(input("Введите значение второго числа " ))
    result = a/b
    return result
print(my_fun())
'''

'''Задача 2
def stud_name(user_name,user_age,surname,city,email,number):
    print(f"Ваc зовут: {user_name} {surname }," + f" вам {user_age} года," + f" ваш город проживания: {city},"f" Ваша почта: {email},"+f" ваш номер телефона: {number}")

stud_name(user_name="Nikita", user_age=32,surname="Olegovich",city="Nadym",email="Nikita@mail.ru",number=9992224441)
stud_name(user_name="Alisa", user_age=23,surname="Viktorovna",city="Moscow",email="Alisa@mail.ru",number=8642134441)
'''


'''Задача 3
def my_func(a, b, c):       
    if a and b>c:
        e =a+b
    if b and c > a:
        e = b + c
    if c and a > b:
        e = c + a
    print(e)        
my_func(5, 4, 5)
'''

'''Задача 4
def my_func(x, y):
    if y == 0:
        return 1
    if y < 0:
        x= 1.0/x
        y= -y
    result= 1
    while y > 0:
        result= result * x
        y -= 1
    return result
print(my_func(float(input("Первое число - ")), int(input("Второе число - "))))
'''


'''Задача 5
a=0
w=0
def my_func():                  #Не совсем понял как можно прекратить цикл после ввода определённого символа после чисел
    global w
    a = input()
    b = sum(map(int, a.split(' ')))
    c=b+w
    w=c
    print(w)
while  a!="":
        my_func()
'''

'''Задача 6
def int_func(text):
    small_word = text[0]
    big_word = chr(ord(small_word) - ord('a') + ord('A'))
    return big_word + text[1:]

first_text = input().split()
res = []
for text in first_text:
    res.append(int_func(text))
print(' '.join(res))
'''
