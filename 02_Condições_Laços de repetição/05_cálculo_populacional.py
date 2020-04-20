'''
Altere o programa anterior permitindo ao usuário informar as populações, nomes e as taxas de
crescimento iniciais. Valide a entrada e permita repetir a operação.
'''

# Resposta:

while True:
    nome_a = input('Infome o nome do país: ').strip().title()
    pais_a = float(input(f'Digite a população inicial do(a) {nome_a}: '))
    p_a = str(pais_a)
    taxa_a = float(input(f'Informe a taxa de crescimento do(a) {nome_a}: '))
    print('*' * 55)
    nome_b = input('Informe o nome do país: ').strip().title()
    pais_b = float(input(f'Digite a população inicial do {nome_b}: '))
    p_b = str(pais_b)
    taxa_b = float(input(f'Informe a taxa de crescimento do(a) {nome_b}: '))
    anos = 0
    print('*' * 55)
    while pais_a <= pais_b:
        pais_a += (pais_a * taxa_a) / 100
        pais_b += (pais_b * taxa_b) / 100
        anos += 1
    break

print('\nDADO:')
print(f'\033[32mPaís 1: {nome_a}\nPopulação inicial: {p_a}..\nTaxa de crescimento: {taxa_a}%\033[m')
print('_' * 55)
print(f'\033[33mPaís 2: {nome_b}\nPolulação inicial: {p_b}..\nTaxa de crescimento: {taxa_b}%\033[m')
print('_' * 55)
print(f'\nEm \033[32m{anos} anos\033[m {nome_a} e {nome_b} terão população igual.\n'
      f'Sendo {pais_a} habitantes!')


print('\n\033[34m@ebony_prog\033[m')