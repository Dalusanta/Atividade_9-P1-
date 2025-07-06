def primos(a):
	for i in range(2, a):
		if a % i == 0:
			return False
	return True

def numeros_primos(num):
	lista = []
	for i in range(2, num+1):
		if primos(i):
			lista.append(i)
	return lista

print(f'      {numeros_primos(43)}')