
def numero_por_extenso(numero):
	""" escreve  o numero por extenso de 0 a 999.999 """

	if type(numero) != int or numero < 0 or numero > 999999:
		return 'Numero incorreto, favor verificar.'

	if numero == 0:
		return 'Zero'

	if numero == 100:
		return 'Cem'

	extenso_list = [
		['', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove'],
		['Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove'],
		['', '', 'Vinte', 'Trinta', 'Quarenta', 'Cinquenta', 'Sessenta', 'Setenta', 'Oitenta', 'Noventa'],
		['', 'Cento', 'Duzentos', 'Trezentos', 'Quatrocentos', 'Quinhentos', 'Seiscentos', 'Setecentos', 'Oitocentos', 'Novecentos']
	]

	# Completa com zeros e divide em 2 trios para o milhar
	numero = str(numero).zfill(6)
	n1 = numero[:3]
	n2 = numero[-3:]
	retorno_list = []

	for n in [n1, n2]:
		cent, dez, und = int(n[0]), int(n[1]), int(n[2])

		# Verifica se tem centena
		if cent != 0:
			retorno_list.append("%s" % extenso_list[3][cent])

		# Verifica se tem dezena
		if dez == 1:
			retorno_list.append("%s" % extenso_list[1][und])

		else:
			if dez != 0:
				retorno_list.append("%s" % extenso_list[2][dez])

			if und != 0:
				retorno_list.append("%s" % extenso_list[0][und])

		# Adiciona a palavra mil apenas no primeiro loop e evita adicionar novamente caso ja exista
		if n == n1 and retorno_list and 'Mil' not in retorno_list:
			retorno_list.append('Mil')


	# Adiciona a juncao 'e' e corrige o 'Mil'
	retorno_extenso = " e ".join(retorno_list)
	retorno_extenso = retorno_extenso.replace('e Mil e', 'Mil,')
	return retorno_extenso


if __name__ == '__main__':
	print('a', numero_por_extenso('a'))
	print(-1, numero_por_extenso(-1))
	print(0, numero_por_extenso(0))
	print(1, numero_por_extenso(1))
	print(10, numero_por_extenso(10))
	print(12, numero_por_extenso(12))
	print(17, numero_por_extenso(17))
	print(35, numero_por_extenso(35))
	print(100, numero_por_extenso(100))
	print(115, numero_por_extenso(115))
	print(123, numero_por_extenso(123))
	print(414, numero_por_extenso(414))
	print(856, numero_por_extenso(856))
	print(1234, numero_por_extenso(1234))
	print(2345, numero_por_extenso(2345))
	print(12345, numero_por_extenso(12345))
	print(123456, numero_por_extenso(123456))
	print(919919, numero_por_extenso(919919))
	print(999999, numero_por_extenso(999999))
	print(1000000, numero_por_extenso(1000000))