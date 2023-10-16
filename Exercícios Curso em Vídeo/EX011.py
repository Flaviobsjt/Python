# Exercício da aula: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la. Sabe-se que cada litro de tinta pinta uma área de 2m²

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area= largura*altura
print('A área da sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura, altura, area))
tinta= area/2
print('Já a quantidade de tinta necessária para pintar essa parede é de {}l'.format(area, tinta))