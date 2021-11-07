def bin2dec(b):
	number = 0
	counter = 0
	for i in b[::-1]: 
		number += int(i)*(2**counter)
		counter += 1

	return str(number)

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
