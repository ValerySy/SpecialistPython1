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
from russian_names import RussianNames

empl_list = [[RussianNames(surname=False, patronymic=False).get_person(),
             RussianNames(name=False, patronymic=False).get_person(),
             random.randint(18,65),
             random.choice(['Экономист', 'Аналитик', 'Маркетолог', 'Программист']),
             random.randint(50000,200000)
             ] for _ in range(100)]
print(empl_list)

