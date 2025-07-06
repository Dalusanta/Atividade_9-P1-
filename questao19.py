import random

def num_int(n):
	if n[0] == '-':
		for i in range(1, len(n)):
			if not n[i].isdigit():
				return False
		return True
	else:
		for i in range(len(n)):
			if not n[i].isdigit():
				return False
		return True
	
def jogo_adivinhacao(n):
	while True:
		rr = ''
		a = 0
		while True:
			a = input(f'Digite um número{rr}: ')
			if num_int(a):
				break
			rr = '(número inválido)'
		
		if int(a) > n:
			print('Maior que o número secreto!')
		elif int(a) < n:
			print('Menor que o número secreto!')
		else:
			print('Parabéns voce acertou!')
			break

jogo_adivinhacao(random.randint(-100, 100))