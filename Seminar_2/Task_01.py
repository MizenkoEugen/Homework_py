# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

n = float(input('Введите вещественное число:'))
if n < 0:
    n = n * (-1)
sum = 0
for i in str(n):
    if i != '.':
        sum += int(i)
print(f'Сумма цифр равна {sum}')

# n = input()
# summ = 0
# for i in n:
#     if i.isdigit():
#         summ+=int(i)
# print(summ)

# n = float(input())
# len_num = len(str(n))-1
# summ=0
# while n!=int(n):
#     n= round(n*10,len_num)
#     print(n)
# while n>0:
#     summ+=n%10
#     n = n//10
# print(summ)
