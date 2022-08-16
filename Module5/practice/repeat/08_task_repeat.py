# Вы решили сделать вклад в банк некоторой суммы на n лет.
# Банк вам предложил x% годовых с расчетом по простым процентам или
# y% годовых по сложным % с периодом капитализации 1 месяц.
# При заданных процентных ставках, определите какой из вкладов вам выгоднее на 5 лет.
# Примечание: формулы расчета простых и сложных процентов ищите на гуглодиске в папке с материалами.


def deposit(a, x, y, n):
    yearly_cap_sum = a
    for i in range(n):
        yearly_cap_sum += a * x /100

    monthly_cap_sum = a * (1 + ((y / 100)/ 12)) ** (n * 12)
    if yearly_cap_sum > monthly_cap_sum:
        return f'X deposit is better ({int(yearly_cap_sum)} with yearly capitalization vs {int(monthly_cap_sum)} ' \
               f'with montly capitalization)'
    else:
        return f'Y deposit is better ({int(yearly_cap_sum)} with yearly capitalization vs {int(monthly_cap_sum)} ' \
               f'with montly capitalization)'

print(deposit(1000000,20,15,3))
