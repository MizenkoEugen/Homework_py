# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def primfactors(n):
   i = 2
   primlist = []
   while i * i <= n:
       while n % i == 0:
           primlist.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primlist.append(round(n))
   return primlist

print(primfactors(int(input('Задайте натуральное число N: '))))