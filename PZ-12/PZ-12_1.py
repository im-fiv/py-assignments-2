'''
Организовать и вывести последовательность из N случайных целых чисел. Из 
исходной последовательности организовать первую последовательность, содержащую 
четные числа, и вторую – для всех остальных. Найти среднее арифметическое в полученных 
последовательностях.
'''

import random

def sort_sequence(n):
    sequence = [random.randint(1, 100) for _ in range(n)]

    numbers_even = [x for x in sequence if x % 2 == 0]
    numbers_odd = [x for x in sequence if x % 2 != 0]

    avg_even = sum(numbers_even) / len(numbers_even) if numbers_even else 0
    avg_odd = sum(numbers_odd) / len(numbers_odd) if numbers_odd else 0

    return sequence, numbers_even, numbers_odd, avg_even, avg_odd

n = 10
sequence, even, odd, avg_even, avg_odd = sort_sequence(n)

print(f'Исходная последовательность: {sequence}')
print(f'Четные числа: {even}')
print(f'Нечетные числа: {odd}')
print(f'Среднее арифметическое четных чисел: {avg_even}')
print(f'Среднее арифметическое нечетных чисел: {avg_odd}')