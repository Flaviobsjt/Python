# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
#de dias pelos quais el foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

km = float(input('Quantos Km foi percorrido pelo carro? '))
dias = int(input('E qual foi a quantidade de dias rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O preço a pagar é de R${}'.format(pago))