'''
Faça um Programa que leia uma lista de 5 números inteiros e mostre-os.
'''

# Resposta:

num = list()

for i in range(5):
    num.append(int(input(f'Digite o {i+1}º número: ')))
print(f'\n{num} ')
print(f'Tipo: {type(num)}')

