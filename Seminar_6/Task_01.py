# Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

# x1 = float(input("Введите x1: "))
# y1 = float(input("Введите y1: "))
# x2 = float(input("Введите x2: "))
# y2 = float(input("Введите y2: "))
# lenght = ((x1 - x2)**2 + (y1 - y2)**2)**(0.5)
# print(round(lenght,10))

# a = [int(input(f'Введите {i} коордитату точки a '))for i in 'xy']
# b = [int(input(f'Введите {i} коордитату точки b '))for i in 'xy']

a = [int(i) for i in input(f'Введите коордитаты точки a через запятую: ').split(',')]
b = [int(i) for i in input(f'Введите коордитаты точки b через запятую: ').split(',')]

lenght = sum([(elem[0] - elem[1])**2 for elem in zip(a,b)])**0.5
print(round(lenght,5))
