# 2)	Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
#     Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class DivisionZero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_zero(divider, denominator):
        try:
            return round(divider / denominator)
        except:
            return f'Деление на ноль недопустимо'


div = DivisionZero(10, 100)
print(DivisionZero.divide_by_zero(10, 0))
print(DivisionZero.divide_by_zero(1, 0.1))
print(div.divide_by_zero(100, 0))
