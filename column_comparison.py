"""
Скрипт считывает текстовый файл или csv с маркировкой кода из честного знака и сравнивает с DataMatrix, который
формируется путем считывания сканером штрихкодов
"""
import csv

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

with open('240314\\Коды из ЧестнЗнака.txt', 'r', encoding='utf-8') as file:
    lines = [f'{line}'.rstrip() for line in file]

with open('240314\\Коды сканир с Упаковок.txt', 'r', encoding='utf-8') as file:
    lines3 = [f'{line}'.rstrip() for line in file]


def find_full_intersection(list1, list2):
    return list(set(list1) & set(list2))

lines4 = [f'{x[2:16]}{x[18:31]}' for x in lines3]

intersection = find_full_intersection(lines, lines4)
print()