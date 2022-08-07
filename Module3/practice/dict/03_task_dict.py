# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]
# Вычислите:
print("Имя и Фамилию сотрудника с самой высокой зарплатой:")

max = 0
index = 0
for i in range(len(staff)):
    if staff[i]['salary'] > max:
        max = staff[i]['salary']
        index = i
print(staff[index]['name'])

print("Имя и Фамилию сотрудника с самой низкой зарплатой:")

# TODO: your code here

print("Среднеарифметическую зарплату всех сотрудников")

# TODO: your code here

print("Количество однофамильцев в организации")

# TODO: your code here

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")

# TODO: your code here
