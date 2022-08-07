# Дан словарь, содержащий данные о товаре из магазина
# "price" - цена товара в валюте "currency"
# "count" - количество товара в магазине
# Считая,что курс доллара равен dollar_rate
# Вычислите стоимость всех товаров с названием "name" в долларах

item = {"name": "Кроссовки", "price": "7540.5", "currency": "rub", "count": "10"}
dollar_rate = 74.12

print(item['name'])
print(item['price'])
print(item['count'])
print(float(item['price']) * float(item['count'])/ dollar_rate)
