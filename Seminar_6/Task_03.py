# Найти произведение пар чисел списка(парой считаем первый и последний
# , второй предпоследний и тд)

# from random import randint

# n = int(input('Введите размер списка '))
# lst = []
# new_lst = []

# for i in range(n):
#     lst.append(randint(0, 9))

# for i in range(int(n//2 + n%2)):
#     a = lst[i] * lst[n - i - 1]
#     new_lst.append(a)

# print(f"{lst} => {new_lst}")

import random
n = int(input('Введите размер списка '))
lst = [random.randint(1, 10) for i in range(n)]
new_lst = [lst[i]*lst[n-i-1] for i in range(int(n//2+n % 2))]
print(f"{lst} => {new_lst}")
