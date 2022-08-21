# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов
import random
lst = [random.randint(-50,50) for _ in range(random.randint(10,20))]
print(lst)
print(len([l for l in lst if l <= 10]))
print(sum([l for l in lst if l > 0]))
print(sum([l for l in lst if l % 2 == 0])/len([l for l in lst if l % 2 == 0]))
