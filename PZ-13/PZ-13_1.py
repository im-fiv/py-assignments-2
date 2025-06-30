'''
В двумерном списке элементы строки N (N задать с клавиатуры) увеличить на 3.
'''

def increment_row(matrix, incr_by, row_num):
	return [[x + incr_by if row == row_num else x for row, x in enumerate(rows)] for rows in matrix]

init_matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

n = int(input('Введите номер строки для увеличения: '))
modif_matrix = increment_row(init_matrix, 3, n)
print(f'Увеличенный список: {modif_matrix}')