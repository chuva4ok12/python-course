# 1)	Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def my_method(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def checking(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 <= year <= 0:
                    return f'Вы все ввели правильно!'
                else:
                    return f'Введите правильный год!'
            else:
                return f'Введите нормальное значение месяца!'
        else:
            return f'Введите корректный день месяца!'
    def __str__(self):
        return f'Текущая дата {Date.my_method(self.day_month_year)}'

today = Date('15 - 12 - 2019')
print(today)
print(Date.checking(17, 10, 2032))
print(today.checking(10, 11, 2020))
print(Date.my_method('11 - 01 - 2017'))
print(Date.checking(1, 13, 2000))


