# Напишите функцию находящую n-ое число Фибоначчи.

def fib_num(n):

    f1 = 0
    f2 = 1

    if n == 1:
        fi = f1
    elif n == 2:
        fi = f2
    elif n > 2:
        i = 3
        fi = 0
        while i <= n:
            fi = f1 + f2
            f1 = f2
            f2 = fi
            i += 1
    return fi

print(fib_num(4))
