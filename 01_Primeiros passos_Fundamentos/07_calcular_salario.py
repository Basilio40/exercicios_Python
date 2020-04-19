''' Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.'''

# Resposta:

ganho_hora = float(input('Informe quanto você recebe por hora: '))
total_hora = float(input('Informe o total de horas trabalhadas: '))
salario = ganho_hora * total_hora
print(f'Salário bruto: R${salario:.2f}')