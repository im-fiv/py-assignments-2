'''
Составить генератор (yield), который преобразует все буквенные символы в 
строчные.
'''

def to_lowercase(input):
	for char in input:
		if 'A' <= char <= 'Z':
			yield char.lower()
		elif 'А' <= char <= 'Я':
			yield char.lower()
		else:
			yield char

input = 'Poterit ne Illud Quidem Adduci Ullus investigandi veri, Nisi Inveneris, et quaerendi defatigatio Turpis est, cum esset Accusata et vituperata ab Hortensio. Qui liber cum et mortem contemnit, Qua qui.'
gen = to_lowercase(input)

input_lowered = ''.join(gen)
print(input_lowered)