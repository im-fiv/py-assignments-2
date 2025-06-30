'''
Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют 
сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно. 
Использовать модуль pickle для сериализации и десериализации объектов Python в 
бинарном формате.
'''

import pickle

class Matrix:
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		self.data = [[0 for _ in range(columns)] for _ in range(rows)]
          
	def __str__(self):
		return '\n'.join([' '.join(map(str, row)) for row in self.data])

	def fill(self, data):
		self.data = data

	def add(self, other):
		result = Matrix(self.rows, self.columns)
		result.data = [[self.data[i][j] + other.data[i][j]
						for j in range(self.columns)]
						for i in range(self.rows)]
		return result

	def sub(self, other):
		result = Matrix(self.rows, self.columns)
		result.data = [[self.data[i][j] - other.data[i][j]
						for j in range(self.columns)]
						for i in range(self.rows)]
		return result

	def mul(self, other):
		result = Matrix(self.rows, other.rows)
		result.data = [[sum(self.data[i][k] * other.data[k][j]
						for k in range(self.columns))
						for j in range(other.rows)]
						for i in range(self.rows)]
		return result

def save_def(filename, matrices):
    with open(filename, 'wb') as f:
        pickle.dump(matrices, f)
	
    print(f'Сохранено {len(matrices)} объектов Matrix в файл {filename}')

def load_def(filename):
    with open(filename, 'rb') as f:
        matrices = pickle.load(f)
	
    print(f'Загружено {len(matrices)} объектов Matrix из файла {filename}')
    return matrices

a = Matrix(2, 3)
a.fill([[1, 2, 3], [4, 5, 6]])

b = Matrix(2, 3)
b.fill([[7, 8, 9], [10, 11, 12]])

c = Matrix(3, 2)
c.fill([[1, 2, 4], [3, 4, 3], [5, 6, 8]])

filename = 'матрицы.pickle'

save_def(filename, [a, b, c])
loaded_matrices = load_def(filename)

for idx, matrix in enumerate(loaded_matrices):
    print(f"\nЗагруженная матрица {idx + 1}:")
    print(matrix)