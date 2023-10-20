# Exercício da aula: Sortear um nome na lista
import random

print('DESCUBRA QUEM É O MAIS...')

quem = ['chato', 'ignorante', 'feliz']
p1 = random.choice(quem)
print('-'*20)
print('Quem é o mais {}'.format(p1))
print('-'*20)

n1 = str(input('Primeira pessoa: '))
n2 = str(input('Segunda pessoa: '))
n3 = str(input('Terceira pessoa: '))
n4 = str(input('Quarta pessoa: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('A pessoa mais {} é {}!'.format(p1, escolhido))