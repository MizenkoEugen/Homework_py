# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibo(n):
    if n >= 0:
        i = range(n+1)
        f = [0, 1]
        for k in i[2:]:
            f.append(f[k-1] + f[k-2])
        return f[n]
    else:
        n = -(n-1)
        i = range(n+1)
        f = [1, 0]
        for k in i[2:]:
            f.append(f[k-2] - f[k-1])
        f.reverse()
    return f[0]

lst = []
n = int(input("Введите число: "))
for i in range(-n, n+1):
    lst.append(fibo(i))
print(lst)
