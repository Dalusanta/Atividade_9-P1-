def maior_numero(a, b, c):
	if a > b and a > c:
		return a
	elif b > a and b > c:
		return b
	else:
		return c
		
print(f'{maior_numero(1,2,3)}')