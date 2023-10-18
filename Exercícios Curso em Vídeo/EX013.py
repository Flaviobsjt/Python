# Exercício da aula: Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

sal = float(input('Qual o salário do funcionário da sua empresa? R$'))
novosal = sal + (sal*15/100)
print('O seu funcionário que ganhava {}, com 15% de aumento, deverá receber R${}'.format(sal, novosal))
