# Иван кладет в банк x рублей под a процентов годовых на n лет. Напишите функцию, которая возвращает число -
# сколько денег получит Иван в результате.

def deposit(x, a, n):
    for i in range(n):
        x += x * a /100
    return x
# функция принимает три числа и возвращает одно - итоговая сумма на счету Ивана.
# Проценты на вклад начисляются один раз в год.

print(deposit(1000000,20,3))
