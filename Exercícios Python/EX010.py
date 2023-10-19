# Exercício da aula: Crie um programa que leia quanto dinheiro uam pessoa tem na carteira e mostre quantos dólares ela  pode comprar
din=float(input('Quanto você tem na carteira? '))
dolar = din/5.04
print('Com R${} você pode comprar US${:.3}'.format(din, dolar))

