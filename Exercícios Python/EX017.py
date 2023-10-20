# Exercício do dia: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
# c2=a2+b2.
from math import hypot

oposto = float(input('Diga o valor do cateto oposto: '))
adjacente = float(input('Diga o valor do cateteo adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print('Tendo {} como cateto oposto e {} como cateto adjacente, o valor da hipotenusa é {:.2f}!'.format(oposto, adjacente, hipotenusa))