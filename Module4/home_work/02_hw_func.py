# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def minimum (*n):
    min_n = n[0]
    for num in n:
        if num < min_n:
            min_n = num
    return min_n


xa = int(input('xa: '))
ya = int(input('ya: '))
xb = int(input('xb: '))
yb = int(input('yb: '))
xc = int(input('xc: '))
yc = int(input('yc: '))

min_distance = minimum(distance(xa, ya, xb, yb), distance(xa, ya, xc, yc), distance(xc, yc, xb, yb))

if min_distance == distance(xa, ya, xb, yb):
    str_name = 'AB'
elif min_distance == distance(xa, ya, xc, yc):
    str_name = 'AC'
else:
    str_name = 'BC'

print(f"Самый короткий отрезок: {str_name}, его длина {min_distance}")  # Выводим название отрезка, например “АС”.
