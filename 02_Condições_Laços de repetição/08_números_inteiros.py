'''
Faça um programa que receba dois números inteiros e gere os números inteiros que estão
no intervalo compreendido por eles.
'''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 < num2:
    for i in range(num1, num2+1):
        print(f'{i} ', end='')
elif num1 > num2:
    for i in range(num1, num2-1, -1):
        print(f'{i} ', end='')
else:
    print('Impossível realizar esta operação com números iguais.')

print('\n\n\033[34m@ebony_prog\033[m')