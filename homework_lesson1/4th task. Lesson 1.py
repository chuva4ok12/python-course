x = int(input('Введите число x:'))
max = 0

while x:
    if x % 10 > max:
        max = x % 10
    x //= 10
print('Максимальная цифра' ':', max)