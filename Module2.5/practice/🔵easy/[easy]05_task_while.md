## "Подсчет положительных"

### Задание

Вводится n целых чисел. \
Посчитайте количество положительных чисел, среди введенных.

### Формат входных данных

Сначала вводится целое положительное n. \
Далее вводится n целых чисел.

### Формат выходных данных

Вывести количество положительных.

### Решение задачи

n = int(input('numbers to check: '))
i = 1
positives_count = 0
while i <= n:
    k = int(input('input ' + str(i) + ' of ' + str(n) + ' number: '))
    if k > 0:
        positives_count += 1
    i += 1
print(str(positives_count) + ' numbers are positive')

---

### Подсказки

<details>
<summary>Подсказка-1</summary>
Смотри пример "Нахождение количества чисел кратных трем в диапазоне [a, b]"
</details>

<details>
<summary>Подсказка-2</summary>
Воспользуйтесь заготовкой кода, дописав недостающие строки:

```python
n = int(input("n: "))
i = 0
num_positive = 0  # Счетчик положительных чисел
while i < n:
    number = int(input("number: "))
    ...
    ...
    # TODO: you code here...
    i += 1
print("Было введено", num_positive, "положительных чисел")
```
</details>

