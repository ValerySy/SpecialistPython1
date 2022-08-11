# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.
import random
#n_a = int(input('n_a: '))
#n_b = int(input('n_b: '))
#n_c = int(input('n_c: '))

a_tuple = (-5, -3, -10, 1, -5, 1, -4, 5, 3, 1)#tuple([random.randint(-10, 10) for _ in range(n_a)])
b_tuple = (-6, -4, 3, 3, 1, -3, 1, -3, -8, -10)#tuple([random.randint(-10, 10) for _ in range(n_b)])
c_tuple = (-2, -1, -4, 5, -6, 1, -10, -5, -8, 0)#tuple([random.randint(-10, 10) for _ in range(n_c)])

print(a_tuple)
print(b_tuple)
print(c_tuple)

elem_count = 0
elem_unique = []
for a in a_tuple:
    if a in b_tuple and a in c_tuple and a not in elem_unique:
        elem_count += 1
        elem_unique.append(a)


print(elem_count)
print(elem_unique)
