# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

my_file = open('test_2.txt', encoding="utf-8")
content = my_file.readlines()
print(f'Содержимое файла: {content}')
print(f'Количество строк в файле - {len(content)}')
for i in range(len(content)):
    print(f'Количество символов {i + 1}-ой строки {len(content[i])}')
my_file = open('test_2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()