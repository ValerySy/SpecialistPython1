#import random
#n = int(input('n: '))
numbers = [2, -5, 8, 9, -25, 25, 4]
numbers_sqrt = []
#for i in range(0, n):
#    numbers.append(random.randint(-100, 100))
    
    
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

for el in numbers:
    #print(int(int(el) ** 0.5), type(int(el) ** 0.5))
    if el > 0 and int(el) % int(el) ** 0.5 == 0:
        numbers_sqrt.append(int(int(el) ** 0.5))
print(numbers, numbers_sqrt)        
