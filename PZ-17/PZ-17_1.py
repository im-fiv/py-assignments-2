'''
Разработать программу с применением пакета tk, взяв в качестве условия одну 
любую задачу из ПЗ №№ 2 – 9.
'''

import tkinter as tk
from tkinter import ttk, messagebox

# Из ПЗ-5.1
def sum_series(n, m):
	sum = 0

	for num in range(n, m + 1):
		sum += num
	
	return sum

def calculate_sum():
	try:
		n = int(n_entry.get())
		m = int(m_entry.get())

		if n > m:
			messagebox.showerror('Ошибка', 'Число n должно быть меньше или равно числу m')
			return
		
		result = sum_series(n, m)
		result_label.config(text=f'Сумма чисел от {n} до {m} = {result}')
	except ValueError:
		messagebox.showerror('Ошибка', 'Введите целые числа')
	except Exception as e:
		messagebox.showerror('Ошибка', f'Неизвестная ошибка: {e}')

root = tk.Tk()
root.title('Сумма ряда чисел')
root.geometry('400x250')

style = ttk.Style()
style.configure('TButton', padding=5, font=('Arial', 10))
style.configure('TLabel', padding=5, font=('Arial', 10))
style.configure('TEntry', padding=5, font=('Arial', 10))

n_label = ttk.Label(root, text='Введите n:')
n_label.pack(pady=(10, 0))

n_entry = ttk.Entry(root)
n_entry.pack()

m_label = ttk.Label(root, text='Введите m:')
m_label.pack()

m_entry = ttk.Entry(root)
m_entry.pack()

calculate_button = ttk.Button(root, text='Вычислить сумму', command=calculate_sum)
calculate_button.pack(pady=10)

result_label = ttk.Label(root, text=' ', font=('Arial', 12, 'bold'))
result_label.pack()

root.mainloop()