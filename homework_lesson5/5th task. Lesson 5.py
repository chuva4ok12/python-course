# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

# def summary():
#     try:
#         with open('test_5.txt', 'w+') as file_obj:
#             line = input('Введите цифры через пробел:')
#             file_obj.writelines(line)
#             my_numb = line.split()
#             print(sum(map(int, my_numb)))
#     except IOError:
#         print('Ошибка в файле')
#     except ValueError:
#         print('Неправильно набран номер. Ошибка ввода-вывода')
# summary()

with open('test_5.txt', 'w') as f:
    nums = input('Введите целые числа через пробел: ')
    f.write('Введенные числа: ' + nums + '\n')
    nums = map(int, nums.split())  # without list
    sum_nums = sum(nums)
    f.write('Сумма чисел: ' + str(sum_nums))
    print('Сумма введенных чисел:', sum_nums)
print('Все записано в файл')
