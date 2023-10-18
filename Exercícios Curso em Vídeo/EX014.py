# Escreva um programa que converta uma temperatura digitada em °C para °F

temperatura = float(input('Informe a tempratura em °C: '))
tempc = (temperatura*1.8) + 32
print('A temperatura de {}°C, corresponde a {}°F!'.format(temperatura, tempc))
