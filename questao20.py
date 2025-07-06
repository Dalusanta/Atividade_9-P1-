def intercalar_listas(a, b):
	if len(a) != len(b):
		return False
	
	new_list = []
	
	for i in range(len(a)):
		new_list.append(a[i])
		new_list.append(b[i])
	
	return new_list

print(intercalar_listas([1, 2, 3], ['a', 'b', 'c']))