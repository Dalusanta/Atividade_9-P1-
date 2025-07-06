def soma_lista(ll):
	sum = 0
	for i in ll:
		sum += i
	return sum

a = []

for i in range(1, 101):
	a.append(i)
	
print(soma_lista(a))