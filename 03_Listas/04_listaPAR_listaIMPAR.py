'''
Faça um Programa que leia 10 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
'''

# Resposta:

num = []
par = []
imp = []

for n in range(10):
    num.append(int(input('Digite um número: ')))
for n in num:
    if n % 2 == 0:
        if n not in par:
            par.append(n)
    else:
        if n not in imp:
            imp.append(n)

print(f'\nNúmeros pares inseridos: {par}\nNúmeros ímpares inseridos: {imp}')

