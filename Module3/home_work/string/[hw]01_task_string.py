# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = "/........,,,,,,,,,,,,"
if text.count('.') > text.count(','):
    print('Точек больше')
elif text.count('.') < text.count(','):
    print('Запятых больше')
else:
    print('Одинаково')
