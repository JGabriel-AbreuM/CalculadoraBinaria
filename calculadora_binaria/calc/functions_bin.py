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
		if (eval(equacao) - int(eval(equacao))) == 0:
			resultado = bin(int(eval(equacao)))[2:]

		else:
			resultado = "Impossível converter um 'float' em binario"
	
	except ZeroDivisionError:
		resultado = "Impossível dividir por 0"

	return resultado 
