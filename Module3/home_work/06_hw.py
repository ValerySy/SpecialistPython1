# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
print("Товары на складе представлены брэндами: ")

new_items = []
for el in items:
    new_items.append(el['brand'])

print(*set(new_items), sep = ', ')
#---------------------------------
print("На складе самый дорогой товар брэнда(ов): ")
max_price = 0
for item in items:
    if item['price'] >= max_price:
        max_price = item['price']
new_items = []
for item in items:
    if item['price'] == max_price:
        new_items.append(item['brand'])
print(*set(new_items), sep = ', ')
#---------------------------------

print("На складе больше всего товаров брэнда(ов): ")

new_items = []
for el in items:
    new_items.append(el['brand'])
brands_unique_list = set(new_items)
brands_assort_list = {brand : new_items.count(brand) for brand in brands_unique_list}

max_count = 0
for brand, brand_assort in brands_assort_list.items():
    if brand_assort > max_count:
        max_count = brand_assort
for brand, brand_assort in brands_assort_list.items():
    if brand_assort == max_count:
        print(brand)
