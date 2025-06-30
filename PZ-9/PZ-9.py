'''
Дана строка 'груши 45 991 63 100 12 морковь 13 47 26 0 16', 
отражающая продажи продукции по дням в кг. Преобразовать информацию из 
строки в словари, с использованием функции найти минимальные продажи по 
каждому виду продукции, результаты вывести на экран.
'''

import re

def extract_sales(input):
    sales = {}
    
    split_input = input.split()
    item = 0
    while item < len(split_input):
        product_name = split_input[item]

        if not re.match(r'^[a-zA-Zа-яА-Я]+$', product_name):
            continue

        sales[product_name] = []
        item += 1

        while item < len(split_input):
            try:
                price = int(split_input[item])
                sales[product_name].append(price)
                item += 1
            except ValueError:
                break

    return sales

sales = extract_sales('груши 45 991 63 100 12 морковь 13 47 26 0 16')
min_sales = {}
for product, sales in sales.items():
    min_sales[product] = min(sales)

print(min_sales)