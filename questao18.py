def senha_segura(ss):
	lgg = 0
	lmm = 0
	nn = 0
	
	if len(ss) >= 8:
		for i in ss:
			if i.isupper():
				lgg +=1
			elif i.islower():
				lmm +=1
			elif i.isdigit():
				nn +=1
		if lgg > 0 and lmm > 0 and nn > 0:
			return True
		else: 
			return False
	else:
		return False

print(senha_segura('aFaf4faf'))