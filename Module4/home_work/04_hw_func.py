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
#---------------------------------------------------------

def drob(chelya, chislitel, znamenatel):
    chislitel = chislitel + chelya * znamenatel
    return chislitel, znamenatel
def plus(chislitel1, znamenatel1, chislitel2, znamenatel2):
    return chislitel1 * znamenatel2\
           + chislitel2 * znamenatel1,\
           znamenatel1 * znamenatel2
def minus(chislitel1, znamenatel1, chislitel2, znamenatel2):
    return chislitel1 * znamenatel2\
           - chislitel2 * znamenatel1,\
           znamenatel1 * znamenatel2
# 111 111/3 + -
stroka = '1 1/3 + 2 + 1/4'
lst = stroka.split(' ')
chislitel1 = None
znamenatel1 = None
chislitel2 = None
znamenatel2 = None
for i in range(len(lst)-1):
    if not '/' in lst[i] and not '+' in lst[i] and not '-' in lst[i]  and not '!' in lst[i]:
        if '/' in lst[i+1]:
            temp_str = lst[i+1].split('/')
            chislitel1, znamenatel1 = drob(int(lst[i]),
                                           int(temp_str[0]), int(temp_str[1]))
            lst[i] = f'{chislitel1}/{znamenatel1}'
            lst[i + 1] = '!'
        else:
            chislitel1 = lst[i]
            znamenatel1 = 1
            lst[i] = f'{chislitel1}/{znamenatel1}'
lst2 = []
for i in range(len(lst)):
    if lst[i] != '!':
        lst2.append(lst[i])
print(lst2)
for i in range(1, len(lst2)-1):
    if lst2[i] == '+':
        temp_str1 = lst2[i - 1].split('/')
        temp_str2 = lst2[i + 1].split('/')
        x1, x2 = plus(int(temp_str1[0]), int(temp_str1[1]), int(temp_str2[0]), int(temp_str2[1]))
        lst2[i+1] = f'{x1}/{x2}'
    elif lst2[i] == '-':
        temp_str1 = lst2[i - 1].split('/')
        temp_str2 = lst2[i + 1].split('/')
        x1, x2 = minus(int(temp_str1[0]), int(temp_str1[1]), int(temp_str2[0]), int(temp_str2[1]))
        lst2[i+1] = f'{x1}/{x2}'
print(lst2[-1])
