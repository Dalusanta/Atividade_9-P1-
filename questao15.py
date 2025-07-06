def analisa_lista(ll):
	ll.sort()
	return ll[-1], ll[0], sum(ll)/len(ll)

lista = [1, 2, 3, 4, 5]
	
print(f'       {analisa_lista(lista)}')