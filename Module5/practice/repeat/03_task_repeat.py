# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

from my_lib import palindrome
a = int(input('a: '))
b = int(input('b: '))

palindrome_count = 0
for i in range(a, b + 1):
    if palindrome(i):
        #print(i)
        palindrome_count += 1

print(palindrome_count)
