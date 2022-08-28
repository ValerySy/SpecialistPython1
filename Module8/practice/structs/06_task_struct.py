# Вы написали программу для работы с сотрудниками и вам ее необходимо протестировать.
# Для теста нужны большие списки сотрудников (100+).
# Вбивать вручную столько данных займет очень много времени.
# Напишите программу, генерирующую списки сотрудников со следующими параметрами:
# 1. Имя
# 2. Фамилия
# 3. Возраст
# 4. Профессия
# 5. Зарплата
# Примечание: Данные сгенерированных сотрудников могут повторяться
import random
names = ['Ivan','Semen','Egor','Anna','Elena','Irina','Vasiliy']
surnames = ['Ivanov','Semenov','Egorov','Annin','Enin','Sergeev','Vasilev']
professions = ['Builder','Manager','Layer','Programmer','Analyst']
result = []

for i in range(100):
    current_worker = {'name': random.choice(names), 'surname': random.choice(surnames),
                     'age': random.randint(18, 80), 'profession': random.choice(professions),
                     'salary': random.randint(50000, 300000)}
    result.append(current_worker)

print(result)




result = [{'name': random.choice(names), 'surname': random.choice(surnames),
                 'age': random.randint(18, 80), 'profession': random.choice(professions),
                 'salary': random.randint(50000, 300000)} for _ in range(100)]
