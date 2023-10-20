# Exercício da aula: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math

ang = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
print('O ângilo de {} tem a TANGENTE de {:.2f}'.format(ang, tang))
