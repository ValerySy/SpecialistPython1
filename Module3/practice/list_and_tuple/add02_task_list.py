# Пользователь вводит на экран дату в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.

# Подсказка: создайте списки с названием дней и названиями месяцев
# Примечание: для экономии времени, можно ограничить номер дня десятью.
# Примечание: склонениями названий можно принебречь
d = input('dd.mm.yyyy: ')

date_list = d.split('.')

days_dict = {1: 'Первое', 2: 'Второе', 3: 'Третье', 4: 'Четвертое', 5: 'Пятое', 6: 'Шестое', 7: 'Седьмое', 8: 'Восьмое', 9: 'Девятое', 10: 'Десятое'}
months_dict = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}

day_text = days_dict[int(date_list[0])]
month_text = months_dict[int(date_list[1])]
print(day_text, ' ', month_text, ' ', date_list[2], ' года')
