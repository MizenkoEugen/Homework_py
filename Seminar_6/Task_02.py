# Найти сумму чисел списка стоящих на нечетной позиции

# lst = list(map(int, input('Задайте список из нескольких чисел через пробел:\n').split()))
# sum = 0
# for i in range(1, len(lst), 2):
#     sum += lst[i]
# print(f"{lst} -> на нечётных позициях элементы {lst[1::2]}, ответ: {sum}")


lst = list(map(int, input('Задайте список из нескольких чисел через пробел:\n').split()))
new_lst = [val for i, val in enumerate(lst) if i%2]
print(f"{lst} -> на нечётных позициях элементы {new_lst}, сумма: {sum(new_lst)}")
