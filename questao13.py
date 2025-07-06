def palindromo(nn):
	nn.lower()
	for i in range(len(nn)):
		if nn[i] != nn[-i-1]:
			return False
	return True
	
print(f'     {palindromo('arara')}')