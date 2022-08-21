# Даны два словаря:
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
# Объедините их в один

dict = {**dictionary_1, **dictionary_2}

print(dict)

dictionary_1.update(dictionary_2)

print(dictionary_1)
