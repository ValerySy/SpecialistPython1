## "Кассовый аппарат"

### Задание
Кассовый аппарат пишет цены всех проданных товаров в текстовый файл, наименование проданных товаров не имеет значение.

По окончанию рабочей недели имеем файл [data/sold.txt](data/sold.txt). \
Товары проданные в один день аппарат записывает на одной строке.

Узнайте:
1. На какую сумму было продано товаров
2. Цену самого дорогого товара
3. Цену самого дешевого товара

### Формат входных данных

Дан текстовый файл. На каждой строке записаны числа(целые или десятичные) разделенные одним или более пробелами.

Количество строк в файле произвольное.

### Формат выходных данных

Вывести:
1. На какую сумму было продано товаров
2. Цену самого дорогого товара
3. Цену самого дешевого товара

### Решение задачи

summa = 0
min_list = []
max_list = []
with open('1.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        max_price = 0
        min_price = float(line.split(' ')[0].rstrip().lstrip())
        for num in line.split(' '):
            if num.rstrip().lstrip().isnumeric():
                summa += float(num.rstrip().lstrip())
                if float(num.rstrip().lstrip()) > max_price:
                    max_price = float(num.rstrip().lstrip())
                if float(num.rstrip().lstrip()) < min_price:
                    min_price = float(num.rstrip().lstrip())
        max_list.append(max_price)
        min_list.append(min_price)

print(summa, max_list, min_list)



```python
# Совет: сначала считайте все цены из файла, сохраните в список,
# преобразовав каждую цену к числу(цены в файле хранятся в виде строк)
# А затем, работам с привычным списком, выполните задания
prices = []
```

---

### Подсказки

<details>
<summary>Подсказка-1</summary>
Для преобразования строки в список вспомните про метод строки .split()

```python
line = "2 4 6 8"
numbers_str = line.split()  # numbers_str = ["2", "4", "6", "8"]
```
</details>

<details>
<summary>Подсказка-2</summary>
Самый простой способ, для преобразования списка строк к списку чисел:

```python
numbers_str = ["2", "4", "6", "8"]
numbers = []
# Пройтись по списку строк:
for el in numbers_str:
    # Каждый элемент списка преобразовать к строке
    number = int(el)
    # и добавить его в новый список
    numbers.append(number)
# numbers = [2, 4, 6, 8]
```
</details>

<details>
<summary>Подсказка-3</summary>
Для объединения списков можно воспользоваться операцией +

```python
list1 = [2, 4, 6]
list2 = ["p", "l"]
list1 += list2  # list1 = [2, 4, 6, "p", "l"]
```
</details>

<details>
<summary>Подсказка-4</summary>
Можете воспользоваться встроенными функциями или написать алгоритмы самостоятельно:

**sum(prices)** - сумма элементов списка prices \
**max(prices)** - максимальный элемент списка \
**min(prices)** - минимальные элемент списка \
</details>
