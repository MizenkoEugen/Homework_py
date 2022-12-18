# Реализуйте алгоритм перемешивания списка.

import random

lst = []
for i in range(5):
    lst.append(random.randint(0,5))
print(f"исходный список:\n{lst}")
random.shuffle(lst)
print(f"список после перемешивания:\n{lst}")