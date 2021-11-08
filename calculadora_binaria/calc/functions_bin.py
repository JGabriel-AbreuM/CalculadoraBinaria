def bin2dec(b):
	num = 0
	count = 0
	for i in b[::-1]: 
		num += int(i)*(2**count)
		count += 1

	return str(num)

def resolve_equacao(sentenca):
	sentenca = sentenca.replace(" ", "")
	equacao = ""
	elemento = ""
	for i in sentenca:
		if i in "+-*/":
			equacao += bin2dec(elemento)
			equacao += i
			elemento = ""

		else:
			elemento += i

	equacao += bin2dec(elemento)
	try:
		resultado = bin(eval(equacao))[2:]
	
	except ZeroDivisionError:
		resultado = "Impossível dividir por 0"

	except TypeError:
		resultado = "Impossível converter um 'float' em binario"
	
	return resultado 
