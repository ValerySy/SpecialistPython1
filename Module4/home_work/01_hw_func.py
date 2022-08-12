# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    first_sum = 0
    second_sum = 0
    for i in range(len(str(ticket_number))):
        if i <=2:
            first_sum += int(str(ticket_number)[i])
        else:
            second_sum += int(str(ticket_number)[i])
    if first_sum == second_sum:
        return True
    else:
        return False

# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
