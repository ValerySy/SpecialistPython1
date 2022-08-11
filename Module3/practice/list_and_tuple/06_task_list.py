# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input('first_number: '))     # Первое число
second_number = int(input('second_number: '))    # Второе число
#lst = [i for i in range[first_number: second_number + 1] if i % 3 == 0]
lst = list(i for i in range(first_number, second_number + 1) if i % 3 == 0)
print(lst)
