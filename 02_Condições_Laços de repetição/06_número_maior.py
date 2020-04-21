'''
Faça um programa que leia 5 números e informe o maior número.
'''

maior = menor = 0
for c in range(6):
    num = int(input(f'Digite o {c}º número: '))
    if c == 0:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num

print(f'\nMaior valor inserido: {maior}\nMenor valor inserido: {menor}')

print('\n\n\033[34m@ebony_prog\033[m')
