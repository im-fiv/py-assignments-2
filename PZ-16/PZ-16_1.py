'''
Создайте класс «Матрица», который имеет атрибуты количества строк и столбцов. 
Добавьте методы для сложения, вычитания и умножения матриц.
'''

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

a = Matrix(2, 3)
a.fill([[1, 2, 3], [4, 5, 6]])

b = Matrix(2, 3)
b.fill([[7, 8, 9], [10, 11, 12]])

c = Matrix(3, 2)
c.fill([[1, 2, 4], [3, 4, 3], [5, 6, 8]])

print('Матрица A:')
print(a)

print('\nМатрица B:')
print(b)

print('\nМатрица C:')
print(c)

matrix_sum = a.add(b)
print(f'\nСумма матриц A и B: {matrix_sum}')

matrix_diff = a.sub(b)
print(f'\nРазность матриц A и B: {matrix_diff}')

matrix_prod = a.mul(c)
print(f'\nПроизведение матриц A и C: {matrix_prod}')