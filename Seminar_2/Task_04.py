# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

N = int(input('Введите число: '))
numbers = []
for i in range(N):
    numbers.append(random.randint(-N,N))
print(numbers)

f = open('file.txt', 'w')
while True:
    s = input('Укажите индекс элемента: ')
    if s == "" or int(s) >= N:
        break
    f.write(s+"\n")
f.close()

result = 1
f = open('file.txt', 'r')
for line in f:
    if line == "":
        break
    result *= numbers[int(line)]
f.close()
print(f'Произведение указанных элементов: {result}')