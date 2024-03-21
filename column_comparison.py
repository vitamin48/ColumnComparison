"""
Скрипт считывает текстовый файл или csv с маркировкой кода из честного знака и сравнивает с DataMatrix, который
формируется путем считывания сканером штрихкодов
"""
import csv

NAME_RESULT_FILE = '240321/дигоксин_difference.txt'


def read_csv():
    # Открываем файл CSV для чтения
    with open('1.csv', newline='', encoding='utf-8') as csvfile:
        # Создаем объект чтения CSV
        csv_reader = csv.reader(csvfile)
        dict_csv = csv.DictReader(csvfile)
        sgtin_lst = []
        # Читаем данные строку за строкой
        for row in dict_csv:
            # row представляет каждую строку в файле CSV как список значений
            sgtin_lst.append(row['sgtin'])
        return sgtin_lst


with open('Коды_честный_знак.txt', 'r', encoding='utf-8') as file:
    znak_lst = [f'{line}'.rstrip() for line in file]

with open('Коды_сканер.txt', 'r', encoding='utf-8') as file:
    scaner_lst = [f'{line}'.rstrip() for line in file]


def find_full_intersection(list1, list2):
    return list(set(list1) & set(list2))


def find_difference(list1, list2):
    return list(set(list1).difference(set(list2)))


lines4 = [f'{x[2:16]}{x[18:31]}' for x in scaner_lst]

intersection = find_full_intersection(znak_lst, lines4)
difference = find_difference(znak_lst, lines4)

print(difference)
print(len(difference))

with open(NAME_RESULT_FILE, 'a') as file:
    file.writelines(diff + '\n' for diff in difference)
