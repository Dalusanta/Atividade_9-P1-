def contador(a, b):
	for i in range(a, b+1):
		print(f'   {i}')

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))

contador(a, b)