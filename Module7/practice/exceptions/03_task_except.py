# Дана строка из пяти целых чисел, разделенных пробелом.
# Пример входных данных: "2 12 -45 7 10"
# Напишите программу, которая находит среди них минимальное положительное число.
# Если таких чисел несколько - вывести любое из них.

# При решении задачи требуется учесть формат входных данных.
# Если входные данные некорректные, сообщить об этом.


is_correct_string = False
while not is_correct_string:
    str_1 = input('input string: ')
    try:
        str_list = set(str_1.split(' '))
        for i in set(str_1.split(' ')):
            if int(i) > 0:
                print(i)
                break

        is_correct_string = True
    except BaseException as err:
        print(err)

