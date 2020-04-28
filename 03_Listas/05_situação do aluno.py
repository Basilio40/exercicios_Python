'''
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima situação final dos alunos permitindo consulta individual.
'''

# Resposta:

from time import sleep
aluno = list()

print('\033[34m-\033[m' * 65)
print('{:^73}'.format('\033[33mB O L E T I M * EBONY.SCHOOL *\033[m'))
print(f'\033[34m{"-" * 65}\033[m')

while True:
    nome = str(input('Nome do aluno: ')).strip().title()
    nota1 = float(input('Insira a primeira nota: '))
    nota2 = float(input('Insira a segunda nota: '))
    nota3 = float(input('Insira a terceira nota: '))
    nota4 = float(input('Insira a quarta nota: '))
    media = float((nota1 + nota2 + nota3 + nota4) / 4)
    aluno.append([nome, [nota1, nota2, nota3, nota4], media])
    sair = str(input('\033[1m\nIncluir outro aluno? [S / N]:\033[m ')).upper().strip()

    while sair not in 'SN':
        sair = str(input('\033[31mTecle [S] para SAIR ou [N] para CONTINUAR: \033[m')).upper().strip()
    if sair == 'N':
        break
    else:
        print('+' * 65)
print()
print('\033[34m-\033[m' * 65)
print('{:^73}'.format('\033[33mB O L E T I M  C O L E T I V O\033[m'))
print(f'\033[34m{"-" * 65}\033[m\n \033[33m{"Cód.":<5}{"| Nome":<51}| {"Média":>5}\033[m')

for i, a in enumerate(aluno):
    print(f' {i:<5}| {a[0]:<49}| {a[2]:>5.1f}')
print('\033[34m-\033[m' * 65)

while True:
    esc = int(input('\nVizualize um aluno ou tecle [999] para sair: '))
    if esc == 999:
        break
    print()
    print('\033[34m-\033[m' * 65)
    print('{:^73}'.format('\033[33mB O L E T I M  I N D I V I D U A L\033[m'))
    print(f'\033[34m{"-" * 65}\033[m\n\033[33m{" Nome":<25}{"| 1ª N. ":<5}{"| 2ª N. ":^5}'
          f'{"| 3ª N. ":^5}{"| 4ª N. ":^5}{"| Média":>5}\033[m')

    if esc <= len(aluno) - 1:
        print(f' {aluno[esc][0]:<24}| {aluno[esc][1][0]:^5} | {aluno[esc][1][1]:^5} '
              f'| {aluno[esc][1][2]:^5} | {aluno[esc][1][3]:^5} | {aluno[esc][2]:>5}')
        print('\033[34m-\033[m' * 65)
        if aluno[esc][2] <= 5:
            status = '\033[31mREPROVADO!\033[m'
        elif 5 < aluno[esc][2] <= 7:
            status = '\033[32mEM RECUPERAÇÃO!\033[m'
        else:
            status = '\033[34mAPROVADO!\033[m'
        print('{:^73}'.format(f' Situação: {status}'))
        print('\033[34m-\033[m' * 65)

    while esc > len(aluno):
        esc = int(input(f'Opção inválida! Tecle um número entre 1 e {len(aluno)}: '))

print('+' * 65, '\n\n{:^73}'.format('\033[31m...finalizando sistema.\033[m\n\n'))
sleep(2)
print('+' * 65, '\n{:^73}'.format('\033[36mSISTEMA FINALIZADO!\033[m'))
print('-' * 65, '\n{:^73}'.format('\033[34m@ebony_prog\033[m'))
print('+' * 65)

