def fatorial(num):
	if num < 0:
		return False
	elif num == 0:
		return 1
	else:
		return num * fatorial(num-1)

print(f'{fatorial(5)}')