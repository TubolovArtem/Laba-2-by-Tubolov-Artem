# Задание №1 (+)
import time
import os


def benin(n):
        red = "\u001b[41m"
        yellow = "\u001b[48;2;255;204;0m"
        green = "\u001b[42m"
        blue = "\u001b[44m"
        black = "\u001b[40m"
        white = "\u001b[47m"
        nV = int(n * 0.2)
        nH = n - nV
        print(green + "\x20" * nV + black + yellow + "\x20" * nH + black)
        print(green + "\x20" * nV + black + red + "\x20" * nH + black)


def clear():
        if os.name == "nt":
                os.system("cls")
        elif os.name == "posix":
                os.system("clear")


benin(10)
time.sleep(5)
clear()

# Задание №2 (+)
import csv

from colours_cfg import colour


def diagram(file_path='./books.csv'):
    with open(file_path, 'r') as books_csv:
        books = list(csv.reader(books_csv, delimiter=';'))[1:]
        before = 0
        after = 0
        for book in books:
            cost = int(book[7].split('.')[0])
            if cost < 150:
                before += 1
            else:
                after += 1
        percent_before = round(before / len(books) * 100, 2)
        percent_after = round(after / len(books) * 100, 2)
        percent_before_str = str(percent_before) + '%'
        percent_after_str = str(percent_after) + '%'
        int_percent_before = int(percent_before_str.split('.')[0])
        int_percent_after = int(percent_after_str.split('.')[0])
        for number in range(100, 0, -2):
            str_to_print = ''
            if number <= int_percent_before:
                str_to_print += ' ' * 12 + colour.white + '   ' + colour.reset + ' ' * 22
            else:
                str_to_print += ' ' * 37
            if number <= int_percent_after:
                str_to_print += '  ' + colour.white + '   ' + colour.reset + '  '
            else:
                str_to_print += ' ' * 37
            if str_to_print != ' ' * 74:
                print(str_to_print)
        print(' ' * 11 + percent_before_str + ' ' * 21 + percent_after_str)
        print('     Книги до 150 рублей      Книги после 150 рублей')
print(diagram())

# Задание №3 (+)
def f(x):
        return x + 1


n = 50
coord = [["\x20" for j in range(n)] for i in range(n)]

for i in range(n):
        coord[n // 2][i] = "-"
        coord[i][n // 2] = "|"

for x in range(n):
        y = f(x)
        if y < n:
                coord[-y][x] = "*"

coord[n // 2][n - 1] = ">"
coord[0][n // 2] = "^"

for i in range(n):
        print("".join(e for e in coord[i]))

# Задание №4 (+)
from colours_cfg import colour


def pattern(amount=5, space=0):
    # 1 строка
    for sth in range(amount):
        print(colour.white, end='')
        print(' ' * 10, end='')
        print(colour.black, end='')
        print(' ' * 4, end='')
        print(colour.white, end='')
        print(' ' * 10, end='')
        print(colour.reset, end='')
        print(' ' * space, end='')
    print('\n', end='')

    # 2 строка
    for sth in range(amount):
        print(colour.white, end='')
        print(' ' * 8, end='')
        print(colour.black, end='')
        print(' ' * 8, end='')
        print(colour.white, end='')
        print(' ' * 8, end='')
        print(colour.reset, end='')
        print(' ' * space, end='')
    print('\n', end='')

    # 3 строка
    for sth in range(amount):
        print(colour.white, end='')
        print(' ' * 6, end='')
        print(colour.black, end='')
        print(' ' * 12, end='')
        print(colour.white, end='')
        print(' ' * 6, end='')
        print(colour.reset, end='')
        print(' ' * space, end='')
    print('\n', end='')

    # 4 строка
    for sth in range(amount):
        print(colour.white, end='')
        print(' ' * 4, end='')
        print(colour.black, end='')
        print(' ' * 16, end='')
        print(colour.white, end='')
        print(' ' * 4, end='')
        print(colour.reset, end='')
        print(' ' * space, end='')
    print('\n', end='')

    # 5 строка
    for sth in range(amount):
        print(colour.white, end='')
        print(' ' * 2, end='')
        print(colour.black, end='')
        print(' ' * 20, end='')
        print(colour.white, end='')
        print(' ' * 2, end='')
        print(colour.reset, end='')
        print(' ' * space, end='')
    print('\n', end='')

    # 6 строка
    for sth in range(amount):
        print(colour.black, end='')
        print(' ' * 24, end='')
        print(colour.reset, end='')
        print(' ' * space, end='')
    print('\n', end='')

    # 7 строка
    for sth in range(amount):
        print(colour.white, end='')
        print(' ' * 2, end='')
        print(colour.black, end='')
        print(' ' * 20, end='')
        print(colour.white, end='')
        print(' ' * 2, end='')
        print(colour.reset, end='')
        print(' ' * space, end='')
    print('\n', end='')

    # 8 строка
    for sth in range(amount):
        print(colour.white, end='')
        print(' ' * 4, end='')
        print(colour.black, end='')
        print(' ' * 16, end='')
        print(colour.white, end='')
        print(' ' * 4, end='')
        print(colour.reset, end='')
        print(' ' * space, end='')
    print('\n', end='')

    # 9 строка
    for sth in range(amount):
        print(colour.white, end='')
        print(' ' * 6, end='')
        print(colour.black, end='')
        print(' ' * 12, end='')
        print(colour.white, end='')
        print(' ' * 6, end='')
        print(colour.reset, end='')
        print(' ' * space, end='')
    print('\n', end='')

    # 10 строка
    for sth in range(amount):
        print(colour.white, end='')
        print(' ' * 8, end='')
        print(colour.black, end='')
        print(' ' * 8, end='')
        print(colour.white, end='')
        print(' ' * 8, end='')
        print(colour.reset, end='')
        print(' ' * space, end='')
    print('\n', end='')

    # 11 строка
    for sth in range(amount):
        print(colour.white, end='')
        print(' ' * 10, end='')
        print(colour.black, end='')
        print(' ' * 4, end='')
        print(colour.white, end='')
        print(' ' * 10, end='')
        print(colour.reset, end='')
        print(' ' * space, end='')
    print('\n', end='')


print(pattern())
