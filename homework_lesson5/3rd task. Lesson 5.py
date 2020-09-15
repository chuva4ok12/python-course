# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# with open('test_3.txt', encoding='utf-8') as f:
#     workers = {}
#     for line in f:
#         key, value = line.split()
#         workers[key] = value
#         if int(value) < 20000:
#             print(f'{key}: зарплата меньше 20000')
with open('test_3.txt', encoding='utf-8') as f:
    salaries = []
    lines = f.readlines()
    for line in lines:
        name, salary = line.split()
        salaries.append(int(salary))
        if int(salary) < 20000:
            print(line)
    print('\nСредняя зарплата:', sum(salaries) / len(salaries))