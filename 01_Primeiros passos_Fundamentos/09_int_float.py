'''
 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a. O produto do dobro do primeiro com metade do segundo.
    b. A soma do triplo do primeiro com o terceiro.
    c. O terceiro elevado ao cubo.'''

# Resposta:

num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))
num3 = float(input('Digite o 3° número: '))
produto = int((num1 * 2) * (num2 / 2))
soma = int((num1 * 3) + num3)
quadrado = float(num3 ** 2)
print(f'Produto do dobro do 1° mais metade do 2°, temos: {produto}')
print(f'Soma do triplo do 1° com 3°, temos: {soma}')
print(f'3° número elevado ao cubo: {quadrado:.2f}')
