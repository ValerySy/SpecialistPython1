# =================================
#             Строки
# =================================

# Строка - это неизменяемая последовательность символов
s = 'Hello'
s2 = "world"
print(s, s2)

# Многострочные строки
s3 = '''Lorem ipsum
dolor sit amet'''

print("-"*10)  # Операция мультипликация - дублирование строки
print(s3)
print("-"*10)  # Добавил для улучшения читабельности вывода

# \n - это один спец. символ - символ переноса строки
s4 = "Lorem ipsum\ndolor sit amet"
print("-"*10)
print(s4)
print("-"*10)
print('s3 == s4 -->', s3 == s4)

s6 = r"Lorem\nipsum\ndolor..."  # "сырая" строка, спецсимволы \n не будут конвертироваться в новые строки
print(s6)

# Операции со строками
print()  # Пустой принт для добавления пустой строки
print("*******Операции со строками********")
# 1. Строки можно складывать:
print('Hello' + ' ' + 'world')
# 2. Если строки идут друг за другом, + можно опустить (конкатенация строк произойдет автоматически):
print('Hello'  ' '  'world')
# 3. Строки повторять операцией *:
print('Hey! ' * 3)

string = 'произвольная строка'
print('string = ', string)
# 4. Получение символа строки по индексу:
# Все элементы строки нумеруются порядковыми индексами (первый индекс - НОЛЬ):
print('string[1] --> ', string[1])

# 5. Срезы
# Подстроку можно получить при помощи срезов:
print('string[6:11] -->', string[6:11])

# Значения по умолчанию: опущенный первый индекс заменяется нулём,
# опущенный второй индекс подменяется размером срезаемой строки.
print('string[6:] -->', string[6:])
print('string[:11] -->', string[:11])

# s6[3] = 'g' # такая конструкция вызовет ошибку, так как строки — неизменяемый объект

# Слишком большой индекс заменяется на размер строки:
print(string[6:100])

# Верхняя граница меньшая нижней возвращает пустую строку:
print('string[50:] -->', string[50:])
print('string[6:1] --> ', string[6:1])

# Индексы могут быть отрицательными числами, обозначая при этом отсчет справа налево:
print('string[-1] -->', string[-1])     # Последний символ
print('string[-2] -->', string[-2])     # Предпоследний символ
print('string[-2:] -->', string[-2:])    # Последние два символа
print('string[:-2] -->', string[:-2])    # Всё, кроме последних двух символов

# Хороший способ понять, как работают срезы - думать о них, как об указателях на места между символами:
#  +---+---+---+---+---+
#  | L | o | r | e | m |
#  +---+---+---+---+---+
#  0   1   2   3   4   5
# -5  -4  -3  -2  -1

# 6. Срезы с шагом
print('string[:12:2] -->', string[:12:2])  # Получаем каждый второй символ для указанного среза
print('string[::-1] -->', string[::-1])    # Переворачиваем строку задом наперед

# 7. Длина строки:
print(len(s))

# 8. Методы строк
print()
print('****Методы строк******')
# Пока воспринимайте метод как функцию, принимающую значение перед точкой в качестве первого аргумента
# 'hello'.upper() воспринимайте как upper('hello')

# Методы строк всегда возвращают новую строку, не изменяя исходную, т.к. строка неизменяемая
print("'иван'.title() -->", 'иван'.title())
print("'python'.upper() -->", 'python'.upper())
print("'трололошка'.find('ло') -->", 'трололошка'.find('ло', 4))  # индекс искомой подстроки (первое вхождение)

# + Подробнее о методах читайте в справочнике по python

----------------------------string
bird = 'ВЫХУХОЛЬ' #str
print(bird[1])
print(bird[-1]) #last symbol
#slices
print(bird[2:4])
print(bird[-5:-3])
print(bird[-3:]) #right 3
print(bird[:3]) #left 3

print(bird[0:8:2]) #each 2 symbol
#bird[from(included):to(excluded):step]

print(len(bird))
print(bird.count('Х'))
print(bird.replace('Х','Д'))

print(bird.find('Х')) # index of 1st symbol
print(bird.rfind('Х')) # index of 1st symbol from right

print(bird.lower()) #
if bird.startswith('В'):
    print(bird)

result = 10
print (f'Result = {result} cows')
print ('Result = {} cows'.format(result))

---------------------list
marks = [3, 4, 4, 5, 4]

fruits = ['banana', 'kiwi', 'pea', 'apple', 'mango']

print(marks[1])

print(fruits) #с квадратными скобками
print(*fruits)
print(fruits[0]) #banaba
print(fruits[0][1]) #a


fruits = [1, 2, 3]
fruits.append(6)
print(fruits)

x = [1, 2, 3]
y = [1, 5]
print(x + y)
print(x * 3)

x[0] = 5
print(x * 3)

---------------dict


phonebook = {} #dict
phonebook['Boris'] = [89686674122, 89668546345]
phonebook['Valeriya'] = 89668546345


useful_things = {}
useful_things['map'] = 123



print(*phonebook['Boris'])
print(phonebook)

for key, value in phonebook.items():
    print(key, value)
    #dict
	
	
	
	---------------------
	x = [1, 2, 2, 2, 6, 6, 8]
print(x)

#set (unique values) changeble
x1 = list(set(x))
print(x1)

