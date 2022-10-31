# Необхідно обчислити коріння квадратного рівняння.
# a · x2 + b · x + c = 0
# Дискримінант рівняння помістіть у змінну D
# D = b2 - 4 · a · c
# Коріння рівняння помістіть у змінні x1 та x2
# x1 = (-b + D0.5) / (2 · a)
# x2 = (-b - D0.5) / (2 · a)
# Виконайте розрахунок коренів для довільних значень коефіцієнтів a, b, c.

import math

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

D = b ** 2 - 4 * a * c

if D>0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("x1: ", x1)
    print("x2: ", x2)
elif D==0:
    x1=-b/2*a
    x2=-b/2*a
    print("x1: ", x1)
    print("x2: ", x2)
else:
    print("No answers!")
