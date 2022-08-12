# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

import re
from fractions import Fraction
s = '-2/3 - -2'
a, op, b = re.split(r'( [+] | [-] )', s)

a = sum([abs(Fraction(x)) for x in a.split()])*(-1 if a[0] == '-' else 1)
b = sum([abs(Fraction(x)) for x in b.split()])*(-1 if b[0] == '-' else 1)
res = eval('a'+op+'b')  # if-elif-else
x, y = res.numerator, res.denominator
if y == 1:
    print(x)
else:
    n, p = divmod(abs(x), y)
    if n:
        print(f'{-n if x<0 else n} {p}/{y}')
    else:
        print(f'{x}/{y}')
