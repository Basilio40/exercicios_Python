'''
Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual
de crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país
A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''

# Resposta:

pais_a = 80000
pais_b = 200000
anos = 0

while pais_a <= pais_b:
    pais_a += pais_a * 0.03
    pais_b += pais_b * 0.015
    anos += 1

print(f'\nEm \033[32m{anos} anos\033[m a população A será igual à B.\n'
      f'Sendo {pais_a} habitantes!')

print('\n\033[34m@ebony_prog\033[m')