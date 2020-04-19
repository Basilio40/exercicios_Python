''' Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    a. Salário bruto.
    b. Quanto pagou ao INSS.
    c. Quanto pagou ao sindicato.
    d. O salário líquido.
    e. Calcule os descontos e o salário líquido. '''

# Resposta:

print('$' * 50)
print('{:^65}'.format('** \033[32mCálculo\033[m ** \033[32mHOLERITE\033[m **'))
print('$' * 50)

ganho_hora = float(input('\nInforme valor recebido por hora: '))
total_hora = int(input('Informe o total de horas trabalhadas: '))
print('')
salario_bruto = float(total_hora * ganho_hora)
imposto_renda = float((salario_bruto * 11) / 100)
inss = float((salario_bruto * 8) / 100)
sindicato = float((salario_bruto * 5) / 100)
salario_liquido = (salario_bruto - sindicato - inss - imposto_renda)

print('\033[32m*\033[m' * 50)
print(f' + Salário Bruto: ', end='')
print('{:.>31}'.format(f' R$ {salario_bruto:.2f}'))
print(f' - Imposto de Renda (11%): ', end='')
print('{:.>22}'.format(f' R$ {imposto_renda:.2f}'))
print(' - INSS (8%): ', end='')
print('{:.>35}'.format(f' R$ {inss:.2f}'))
print(' - Sindicato (5%): ', end='')
print('{:.>30}'.format(f' R$ {sindicato:.2f}'))
print(' = Salário líquido: ', end='')
print('{:.>29}'.format(f' R$ {salario_liquido:.2f}'))
print('\033[32m*\033[m' * 50)
