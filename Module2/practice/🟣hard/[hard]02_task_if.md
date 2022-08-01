## "Шахматы: слон"

### Задание

Требуется определить, бьет ли слон, стоящий на клетке с указанными координатами (номер строки и номер столбца), фигуру, стоящую на другой указанной клетке.

### Формат входных данных

Даны четыре числа целые числа в диапазоне [1, 8], координаты слона и координаты другой фигуры

### Формат выходных данных

Вывести "Да", если слон бьет фигуру или "Нет", если не бьет.

### Решение задачи

sx = int(input('Insert x for Bishop piece:'))
sy = int(input('Insert x for Bishop piece:'))
x = int(input('Insert x for Other piece:'))
y = int(input('Insert x for Other piece:'))

i = 0
yesCount = 0

while (1<= sx + i <=8 and 1<= sy + i <=8) or (1<= sx - i <=8 and 1<= sy + i <=8) or (1<= sx + i <=8 and 1<= sy - i <=8) or (1<= sx - i <=8 and 1<= sy - i <=8):
    if (sx + i == x and sy + i == y) or (sx - i == x and sy + i == y) or (sx + i == x and sy - i == y) or (sx - i == x and sy - i == y):
        yesCount+= 1
    #print(sx + i, sy + i ,sx - i, sy + i ,sx + i, sy - i ,sx - i, sy - i )
    i+= 1   
#print(i,yesCount)    
if yesCount > 0:
    print('Yes')
else:
    print('No')    

---
