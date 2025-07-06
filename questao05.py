def e_par(num):
	if num % 2 == 0:
		return True
	else:
		return False
		
n = int(input('Digite um númeto: '))

if e_par(n):
	print('É par!')
else:
	print('É ímpar!')