'''
Приложение АПТЕКА для автоматизации работы аптечных пунктов. Таблица 
Лекарственные Средства должна содержать следующую информацию: Код, Название 
препарата, Применение, Количество, Цена, Страна-производитель.
'''

import sqlite3

DATABASE_NAME = 'apteka.db'
conn = sqlite3.connect(DATABASE_NAME)

def create_table():
	cursor = conn.cursor()
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS ЛекарственныеСредства (
			Код INTEGER PRIMARY KEY,
			НазваниеПрепарата TEXT NOT NULL,
			Применение TEXT,
			Количество INTEGER,
			Цена REAL,
			СтранаПроизводитель TEXT
		)
	''')
	conn.commit()

def insert_data(data_count=1):
	cursor = conn.cursor()
	for _ in range(data_count):
		code = int(input('Код: '))
		name = input('Название: ')
		application = input('Применение: ')
		count = int(input('Количество: '))
		price = float(input('Цена: '))
		country = input('Страна: ')
		cursor.execute('''
			INSERT INTO ЛекарственныеСредства (Код, НазваниеПрепарата, Применение, Количество, Цена, СтранаПроизводитель)
			VALUES (?, ?, ?, ?, ?, ?)
		''', (code, name, application, count, price, country))
	conn.commit()

def select_data():
	cursor = conn.cursor()
	name = input('Название для поиска: ')
	cursor.execute('SELECT * FROM ЛекарственныеСредства WHERE НазваниеПрепарата = ?', (name,))
	results = cursor.fetchall()
	for row in results:
		print(row)

def delete_data():
	cursor = conn.cursor()
	name = input('Название для удаления: ')
	cursor.execute('DELETE FROM ЛекарственныеСредства WHERE НазваниеПрепарата = ?', (name,))
	conn.commit()

def update_data():
	cursor = conn.cursor()
	name = input('Название для редактирования: ')
	price = float(input('Новая цена: '))
	cursor.execute('UPDATE ЛекарственныеСредства SET Цена = ? WHERE НазваниеПрепарата = ?', (price, name))
	conn.commit()

create_table()
while True:
	print('1. Ввод, 2. Поиск, 3. Удаление, 4. Редактирование, 5. Выход')
	choice = input('Действие: ')
	if choice == '1': insert_data()
	elif choice == '2': select_data()
	elif choice == '3': delete_data()
	elif choice == '4': update_data()
	elif choice == '5': break
	else: break