# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.

def last_sheet(num_items, items_on_page):
    if num_items % items_on_page:
        return num_items % items_on_page
    else:
        return items_on_page


print(last_sheet(13356,342))
