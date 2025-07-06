def contar_vogais(pp):
	c = 0
	pp.lower()
	for i in pp:
		if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
			c += 1
	return c

print(f'     {contar_vogais('python')}')