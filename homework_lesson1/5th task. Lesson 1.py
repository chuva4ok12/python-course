profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print("Фирма работает с прибылью. Рентабельность выручки составила ", profit / costs)
    workers = int(input("Введите количество сотрудников фирмы "))
    print("прибыль фирмы в расчете на одного сотрудника составила ", profit / workers)
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")