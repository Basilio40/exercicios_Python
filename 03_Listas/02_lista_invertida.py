'''
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''

# Resposta:

num = []

for i in range(10):
    num.append(float(input(f'Digite o {i+1}º número real: ')))

print(f'\n Lista na ordem: {num}')
num.reverse()
print(f'Lista invertida: {num}')
