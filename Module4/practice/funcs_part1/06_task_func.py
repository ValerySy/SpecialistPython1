# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:

def point_in_circle(x, y, xc, yc, r):
    if (xc - x) ** 2 + (yc - y) ** 2 < r ** 2:
        return True
    else:
        return False
# Не забудьте протестировать вашу функцию

print(point_in_circle(0, 0, 6, 6, 2))
