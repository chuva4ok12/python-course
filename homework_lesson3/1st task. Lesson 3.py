# 1. Реализовать  функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.
def div(*args):
    try:
        arg1 = int(input("Input dividend "))
        arg2 = int(input("Input divider "))
        res = arg1 / arg2
    except ZeroDivisionError:
        return "Wrong divider! You can't use zero as a divider"
    return res

print(div())
