# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(map(int, input("Задайте последовательность чисел через пробел:\n").split()))
new_lst = []

[new_lst.append(i) for i in lst if lst.count(i) == 1]

# for i in lst:
#     if lst.count(i) == 1:
#         new_lst.append(i)

print(f"{lst} => {new_lst}")


