# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

import random

n = int(input('n: '))
lst = [random.randint(-10, 10) for _ in range(n)]
print(lst)
print(sum(lst))
