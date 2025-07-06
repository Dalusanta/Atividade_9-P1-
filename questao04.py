def med(a, b, c):
	return (a+b+c)/3

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))

print(f'A média de {a}, {b} e {c} é igual a {med(a, b, c):.2f}.')