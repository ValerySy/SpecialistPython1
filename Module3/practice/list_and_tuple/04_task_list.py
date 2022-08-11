# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

import random

n = int(input('n: '))
lst = [random.randint(-10, 10) for _ in range(n)]
positive_items_sum = 0
for item in lst:
    if item > 0:
        positive_items_sum += item
print(lst)
print(sum(lst))
print(positive_items_sum)
