# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

n = int(input('Введите размер списка '))
lst = []
new_lst = []

for i in range(n):
    lst.append(randint(0, 9))

for i in range(int(n/2 + 1)):
    a = lst[i] * lst[n - i - 1]
    new_lst.append(a)

print(f"{lst} => {new_lst}")
