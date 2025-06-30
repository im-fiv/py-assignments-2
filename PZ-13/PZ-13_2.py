'''
В двумерном списке элементы последнего столбца заменить на -1.
'''

def replace_last_column(matrix, value):
	return [row[:-1] + [value] for row in matrix]

init_matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

modif_matrix = replace_last_column(init_matrix, -1)
print(f'Измененная матрица:\n{modif_matrix}')