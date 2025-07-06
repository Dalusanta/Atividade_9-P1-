def repetir_mensagem(mm, nn):
	for i in range(nn):
		print(mm)

men = input('Digite uma mensagem: ')
a = int(input('Número de vezes: '))

repetir_mensagem(men, a)