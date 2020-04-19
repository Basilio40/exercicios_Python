''' Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).'''

# Resposta:

far = float(input('Informe a temperatura em Fahrenheit: '))
cel = int((5 * (far - 32) / 9))
print(f'Convertendo {far}F° para Celsius, temos: {cel}C°')
