## "Подсчет гласных букв"

### Задание

Подсчитать количество гласных(русских) букв во введенной строке без учета регистра.

### Формат входных данных

Дана произвольная строка.

### Формат выходных данных

Вывести количество гласных букв.

### Решение задачи

text = "В теории, теория и практика неразделимы. На практике это не так."
text1 = text.lower()
vowels = "ауоыэяюёие"
# TODO: you code here...
vowels_count = 0
for sym in text1:
    if sym in vowels:
        vowels_count += 1
print(vowels_count)
---

### Подсказки

<details>
<summary>Подсказка-1</summary>
Преобразуйте исходную строку к нижнему регистру воспользовавшись соответствующим методом.
</details>
