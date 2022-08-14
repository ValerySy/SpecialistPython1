# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.
import random

def gen_list(size, of, to):

    return [random.randint(of, to) for _ in range (size) ]

print(gen_list(10, -5, 5))
