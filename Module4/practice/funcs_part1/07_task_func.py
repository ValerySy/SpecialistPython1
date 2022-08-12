# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43

def sec_in_time(sec):
    hours = sec // 3600
    minutes = (sec - 3600 * hours) // 60
    seconds = sec - 3600 * hours - 60 * minutes

    if 0 <= hours <= 9:
        hours_str = '0' + str(hours)
    else:
        hours_str = str(hours)

    if 0 <= minutes <= 9:
        minutes_str = '0' + str(minutes)
    else:
        minutes_str = str(minutes)

    if 0 <= seconds <= 9:
        seconds_str = '0' + str(seconds)
    else:
        seconds_str = str(seconds)

    return hours_str + ':' + minutes_str + ':' + seconds_str



print(sec_in_time(29143))
