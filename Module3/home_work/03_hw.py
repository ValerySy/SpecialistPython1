# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
n = int(input('n: '))
numbers = []
for i in range(0, n):
    numbers.append(random.randint(-100, 100))
    
    
el_sum = 0    
    
for el in numbers:
    if int(el) > 0 and int(el) % 2 == 0:
        el_sum += int(el)

print(numbers, el_sum)   
# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
# TODO: your code here
