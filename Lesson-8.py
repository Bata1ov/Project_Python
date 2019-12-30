'''Задача 1
class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        print(cls, date_as_string)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year <= 2999:
            print(date_as_string)
            return day, month, year
        else:
            print('Ошибка ввода данных')


d = '30-12-2019'
date2 = Date.from_string(d)
is_date = Date.is_date_valid(d)
'''

'''Задача 2
class MyException(Exception):

    def division_func(self, a, b):
        try:
            res = round(a / b, 2)
        except ZeroDivisionError:
            print(f"{a} / {b} -> на ноль делить нельзя!\n")
        else:
            print(f"{a} / {b} = {res} \n")


m_e = MyException()

m_e.division_func(1, 2)
m_e.division_func(1, 0)
'''

'''Задача 3
class IntException(Exception):
    def __init__(self):
        self.txt = 'Введено не число '


res_list = []
while True:
    inp_user = input('Введите число или Enter для выхода ')
    if inp_user == '':
        break
    else:
        try:
            if inp_user.isdigit():
                res_list.append(int(inp_user))
            elif inp_user.count('.') > 1:
                raise IntException
            else:
                for sym in inp_user:
                    if not sym.isdigit() and sym != '.':
                        raise IntException
                res_list.append(float(inp_user))
        except IntException as err:
            print(err.txt)
print(res_list)
'''


'''Задача 4.5.6 
class Warehouse:
    office_equipment = {}

    def __init__(self):
        self.useful_volume = Warehouse.is_it_right_type(input("Чтобы начать работу,укажите объём вашего склада:\n"), float)
        self.residual_volume = self.useful_volume

    # Реализуе типизацию ввода
    @classmethod
    def is_it_right_type(cls, some_var, needed_type):
        while True:
            if some_var == "":
                some_var = input("Введена пустая строка. Повторите ввод.\n")
                continue
            try:
                some_var = needed_type(some_var)
                if type(some_var) in {int, float} and some_var <= 0:
                    some_var = input("Нужно вводить положительное число.\n")
                    continue
            except ValueError:
                if needed_type == int:
                    some_var = input("Нужно вводить целое число.\n")
                elif needed_type == float:
                    some_var = input("Нужно вводить число.\n")
                else:
                    some_var = input("Нужно вводить строку.\n")
                continue
            break
        return some_var

    @classmethod # Когда будем добавлять технику потребуется для выбора пунктов
    def two_variants(cls, some_var):
        while True:
            some_var = cls.is_it_right_type(some_var, int)
            if some_var not in {1, 2}:
                some_var = input("Нужно ввести 1 или 2.\n")
                continue
            break
        return some_var

    # Процедура добавления на склад.
    def warehouse_input(self, type_office_equipment, quality__input):
        quality__input = self.is_it_right_type(quality__input, int)
        input_volume = self.is_it_right_type(type_office_equipment.volume, float) * quality__input
        # Наименование техники
        warehouse_item = " ".join([type_office_equipment.name, type_office_equipment.brand_model])
        # Реализация добавления техники той же марки, с другими характеристиками
        fullname_item = " ".join(map(str, type_office_equipment.__dict__.values()))
        if self.residual_volume - input_volume >= 0:
            self.residual_volume -= input_volume
            # if - добавить технику на скалд; else: if - Уже имеется и добавляем к ним; else: else - нету свободного места .
            if Warehouse.office_equipment.get(warehouse_item) is None:
                Warehouse.office_equipment[warehouse_item] = [quality__input, type_office_equipment.__dict__]
                print(f"На склад добавлены {warehouse_item} в количестве {quality__input} шт., "
                      f"всего на складе {Warehouse.office_equipment[warehouse_item][0]} шт.")
            else:
                if " ".join(map(str, Warehouse.office_equipment[warehouse_item][1].values())) == fullname_item:
                    Warehouse.office_equipment[warehouse_item][0] += quality__input
                    print(f"На склад добавлены {warehouse_item} в количестве {quality__input} шт., "
                          f"всего на складе {Warehouse.office_equipment[warehouse_item][0]} шт.")
                else:
                    print(f"На складе обнаружен {warehouse_item}, но его характеристики отличаются от введённых Вами. "
                          f"Внимательно проверьте данные и попробуйте ещё раз.")
        else:
            print(f"Недостаточно свободного места на складе.")

    # Процедура изъятия со склада.
    def warehouse_output(self, warehouse_item, quality__output):
        quality__output = self.is_it_right_type(quality__output, int)
        # if - нет такой техники; elif - нет такой в таком количестве; else - забрали.
        if Warehouse.office_equipment.get(warehouse_item) is None:
            print(f"Данный {warehouse_item} на складе не обнаружен.")
        elif Warehouse.office_equipment[warehouse_item][0] < quality__output:
            print(f"Нельзя выдать {quality__output} шт. {warehouse_item}")
        else:
            output_volume = Warehouse.office_equipment[warehouse_item][1]["volume"] * quality__output
            self.residual_volume += output_volume
            Warehouse.office_equipment[warehouse_item][0] -= quality__output
            print(f"Переданы {warehouse_item} в количестве {quality__output} шт")


class OfficeEquipment:
    def __init__(self):
        self.brand_model = Warehouse.is_it_right_type(input("Введите название марки и модели:\n"), str)
        self.volume = Warehouse.is_it_right_type(input("Введите занимаемый объём (с упаковкой):\n"), float)


# наследник от техники
class PrintingOfficeEquipment(OfficeEquipment):
    def __init__(self):
        super().__init__()
        is_it_colored = {1: "чёрно-белый", 2: "цветной"}
        self.is_it_colored = is_it_colored[
            Warehouse.two_variants(
                input(
                    "Укажите тип печати и/или сканирования:\n"
                    "[1] - чёрно-белый;\n"
                    "[2] - цветной.\n"
                )
            )
        ]


class Printer(PrintingOfficeEquipment):
    def __init__(self):
        self.name = "принтер"
        super().__init__()
        self.printing_speed = Warehouse.is_it_right_type(input("Введите скорость печати, лист/мин:\n"), int)
        print_type = {1: "струйная", 2: "лазерная"}
        self.print_type = print_type[
            Warehouse.two_variants(
                input(
                    "Укажите метод печати:\n"
                    "[1] - струйная;\n"
                    "[2] - лазерная.\n"
                )
            )
        ]


class Scanner(PrintingOfficeEquipment):
    def __init__(self):
        self.name = "сканер"
        super().__init__()
        self.scanning_speed = Warehouse.is_it_right_type(input("Введите скорость сканирования, лист/мин:\n"), int)

w = Warehouse()
user_choice = 0

while user_choice < 5:
    user_choice = Warehouse.is_it_right_type(
        input("Что вы хотите сделать?\n"
              "[1] - добавить технику на склад;\n"
              "[2] - забрать технику со склада;\n"
              "[3] - узнать свободное место;\n"
              "[другая цифра] - завершить работу со складом.\n"),
        int
    )

    if user_choice in {1, 2}:

        in_or_out = {1: "Что вы хотите добавить на склад?\n", 2: "Что вы хотите забрать со склада?\n"}

        user_choice_tech = Warehouse.is_it_right_type(
            input(f"{in_or_out[user_choice]}"
                  "[1] - принтер;\n"
                  "[2] - сканер;\n"
                  "[другая цифра] - возврат в предыдущее меню.\n"),
            int
        )

        if user_choice == 1:
            if user_choice_tech == 1:
                obj = Printer()
            elif user_choice_tech == 2:
                obj = Scanner()
            else:
                continue
            w.warehouse_input(obj, input("Сколько штук?\n"))
            continue

        if user_choice == 2:
            if user_choice_tech == 1:
                name = "принтер"
            elif user_choice_tech == 2:
                name = "сканер"
            else:
                continue
            w.warehouse_output(" ".join([name, input("Введите название модели:\n")]),
                               input("Сколько забрать?\n"))
            continue

    if user_choice == 3:
        print(f"Свободный объём на складе {round(w.residual_volume, 3)} м^3.\n")

print("Вы выбрали окончание работы.")
'''


'''Задача 7
class MyComplex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '(%s+%sj)' % (self.a, self.b)

    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return MyComplex(new_a, new_b)

    def __mul__(self, other):
        new_a = self.a * other.a - self.b * other.b
        new_b = self.b * other.a + self.a * other.b
        return MyComplex(new_a, new_b)


z1 = MyComplex(1, 2)
z2 = MyComplex(2, 3)

print(f"{z1} + {z2} = ", z1 + z2)
print(f"{z1} * {z2} = ", z1 * z2)
'''
