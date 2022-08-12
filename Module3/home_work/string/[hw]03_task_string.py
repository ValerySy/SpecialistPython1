# Посчитайте количество согласных букв в данной строке.

text = 'аовпттлфурвыодфлрыовимфри'
consonants = 'бвгджзйклмнпрстфхцчшщ'

count_consonants = 0

for letter in text:
    if letter in consonants:
        count_consonants += 1
print('Количество согласных букв: ', count_consonants)
