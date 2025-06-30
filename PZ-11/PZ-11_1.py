'''
Средствами языка Python сформировать текстовый файл (.txt), содержащий 
последовательность из целых положительных и отрицательных чисел. Сформировать 
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую 
обработку элементов: 
Исходные данные: 
Количество элементов: 
Среднее арифметическое элементов: 
Положительные четные элементы: 
Сумма положительных четных элементов: 
Среднее арифметическое положительных четных элементов:
'''

import random

def process_file(input_filename, output_filename):
    with open(input_filename, 'r') as f:
        line = f.readline()
        numbers = [int(x) for x in line.split()]

    number_count = len(numbers)
    number_avg = sum(numbers) / number_count if number_count > 0 else 0
    positive_even = [x for x in numbers if x > 0 and x % 2 == 0]
    positive_even_sum = sum(positive_even)
    positive_even_avg = positive_even_sum / len(positive_even) if positive_even else 0

    with open(output_filename, 'w', encoding='utf8') as f:
        f.write(f'Исходные данные: {line}\n')
        f.write(f'Количество элементов: {number_count}\n')
        f.write(f'Среднее арифметическое элементов: {number_avg}\n')
        f.write(f'Положительные четные элементы: {positive_even}\n')
        f.write(f'Сумма положительных четных элементов: {positive_even_sum}\n')
        f.write(f'Среднее арифметическое положительных четных элементов: {positive_even_avg}\n')

input_filename = 'исходные_числа.txt'
output_filename = 'результаты.txt'
number_count = 10

with open(input_filename, 'w') as f:
    for _ in range(number_count):
        number = random.randint(-100, 100)
        f.write(str(number) + ' ')

process_file(input_filename, output_filename)