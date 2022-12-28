# Задана натуральная степень koef. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени koef.
# Пример:- koef=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input("Задайте натуральную степень k: "))
koef = [random.randint(0, 101) for i in range(k+1)]
str = ''
if len(koef) <= 1:
    str = 'x = 0'
else:
    for i in range(len(koef)):
        if i < len(koef) - 2 and koef[i] != 0:
            str += f'{koef[i]}x^{len(koef)-i-1} + '
        elif i == len(koef) - 2 and koef[i] != 0:
            str += f'{koef[i]}x'
            if koef[i+1] != 0:
                str += ' + '
        elif i == len(koef) - 1 and koef[i] != 0:
            str += f'{koef[i]} = 0'
        elif i == len(koef) - 1 and koef[i] == 0:
            str += ' = 0'

print(str)
file = open('file.txt', 'a')
file.write(str)
file.close()
