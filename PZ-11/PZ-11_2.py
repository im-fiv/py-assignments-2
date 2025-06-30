'''
Из предложенного текстового файла (text18-7.txt) вывести на экран его содержимое, 
количество букв в нижнем регистре. Сформировать новый файл, в который поместить текст 
в стихотворной форме предварительно поставив последнюю строку между второй и 
третьей.
'''

input_filename = 'text18-7.txt'
output_filename = 'output.txt'

with open(input_filename, 'r', encoding='utf-8') as f:
	lines = f.readlines()

print('Содержимое файла:')
for line in lines:
	print(line, end='')

# Подсчет букв в нижнем регистре
lowercase_count = 0
for line in lines:
	for char in line:
		if 'a' <= char <= 'z' or 'а' <= char <= 'я':
			lowercase_count += 1

if len(lines) >= 3:
	last_line = lines.pop()
	lines.insert(2, last_line)

with open(output_filename, 'w', encoding='utf-8') as f:
	f.writelines(lines)