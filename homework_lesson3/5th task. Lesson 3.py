# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже
# подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

result = 0
while True:
    line = input("Enter number or special token q for exit: ")
    tokens = line.split()
    for token in tokens:
        try:
            number = float(token)
            result += number
        except:
            if token == 'q':
                print(f"You sum is {result}. Program is terminated")
                exit(0)
            else:
                print(f"You sum is {result}. Input error", file=sys.stderr)
                exit(1)

print(result)
exit()

# def summary():
#     ex = False
#     result = 0
#     while ex == False:
#         numbers = input('Enter numbers or q to exit: ').split()
#         res_line = 0
#         for num in numbers:
#             if 'q' in num:
#                 ex = True
#                 break
#             res_line += int(num)
#         result += res_line
#     print(result)

