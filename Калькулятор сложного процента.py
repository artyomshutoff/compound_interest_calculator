# -*- coding: utf-8 -*-
"""
@author: artyomshutoff
"""

def nice_num(n):
	a = [i for i in str(int(n))][::-1]
	out = ''
	c = 0
	for i in a:
		if c%3 == 0 and c != 0:
			out += ' '
		out += i
		c += 1
	
	return out[::-1]

def compound_interest_calculator(percent=8, amount=25000, start=25, stop=35, month=True) -> str:
	"""
	Parameters
	----------
	percent : int
		Процент, начисляемый на капитал в раз год.
	amount : int
		Откладываемая сумма каждый год.
	start : int
		Начало создания капитала.
	stop : float
		Конечная дата создания капитала.
	month : int
		True или False если нужно указать сумму, которую будем откладывать за месяц, а не за год.
	Returns
	-------
	Возможный капитал и пенсия к концу конечной даты.
	"""

	amount *= 12 if month else 1

	out = amount

	for i in range(start, stop):
		out *= 1 + percent/100
		out += amount

	return 'Ваш возможный капитал: ' + nice_num(out) + '\n' + 'Ваша возможная пенсия: ' + nice_num(out * (percent/100) / 12)

print(compound_interest_calculator(8, 25000, 25, 35, month=True))