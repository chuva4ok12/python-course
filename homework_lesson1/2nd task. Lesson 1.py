time = int(input("Введите время в секундах: "))
min = 60
hour = 60 * 60

HOUR = time // hour
MINUT = (time - (HOUR * hour)) // min
SECONDS = time - ((HOUR * hour) + (MINUT * min))



print('{}чч:{}мм:{}сс'.format(HOUR, MINUT, SECONDS))