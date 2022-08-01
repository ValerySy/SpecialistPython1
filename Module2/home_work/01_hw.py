# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Формат входных данных
# Вводятся 3 натуральных числа n, m и k. Точно известно, что  k ≠ n ⋅ m.
# Формат выходных данных
# Выведите «YES», если можно отломить от шоколадки ровно k долек, и «NO» иначе.

n = int(input('Input n:'))
m = int(input('Input m:'))
k = int(input('Input k:'))

x = 1
yCount = 0

while x * k <= n or x * k <= m:
    if n * x == k or m * x == k:
        yCount+= 1
    x+= 1
if yCount > 0:
    print('Yes')
else: 
    if k == n * m:
        print('Ohhh! Take a whole chocko sweet tooth :)')
    else:    
        print('No')    
