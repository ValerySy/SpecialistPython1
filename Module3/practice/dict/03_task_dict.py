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
print(staff[index]['name'], staff[index]['surname'], sep = " ")
#---------------------------------------------------------------------
print("Имя и Фамилию сотрудника с самой низкой зарплатой:")
min_salary = staff[0]['salary']
for i in range(len(staff)):
    if staff[i]['salary'] < min_salary:
        min_salary = staff[i]['salary']
for i in range(len(staff)):
    if staff[i]['salary'] == min_salary:
        print(staff[i]['name'], staff[i]['surname'], sep=" ")

print("Среднеарифметическую зарплату всех сотрудников")
#----------------------------------------------------------------
empl_total_salary = 0
for empl in staff:
    empl_total_salary += empl['salary']
print(int(empl_total_salary/len(staff)))
#----------------------------------------------------------------
print("Количество однофамильцев в организации")
surname_list = []
for el in staff:
    surname_list.append(el['surname'])
surname_unique_list = set(surname_list)
surname_dict = {surname : surname_list.count(surname) for surname in surname_unique_list}
for surname, surname_count in surname_dict.items():
    if surname_count > 1:
        print(surname, surname_count)
#----------------------------------------------------------------
print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")

for el in sorted(staff, key=lambda salary_value: salary_value['salary']):
    print(el['name'], el['surname'])
