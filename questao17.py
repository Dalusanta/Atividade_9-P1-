import random

def simular_dado(n):
	lista =[]
	for i in range(n):
		lista.append(random.randint(1,6))
	return lista
	
for i in range(11):
	print(f'{simular_dado(i)} -> {i}')