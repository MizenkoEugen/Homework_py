# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input('Введите цифру, обозначающую день недели: '))
if a < 1 or a > 7:
    print(f'{a} Не является днем недели.')
else:
    if a == 6 or a == 7:
        print(f'{a} Выходной день')
    else: 
        a > 0 and a < 6
        print(f'{a} Рабочий день')
