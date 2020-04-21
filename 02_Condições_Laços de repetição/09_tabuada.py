'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

Tabuada:
5 X 1 = 5
5 X 2 = 10
(:)
5 X 10 = 50
'''


print('\033[32m#\033[m' * 40)
print('{:-^40}'.format(' TABUÁDA '))
print('\033[32m#\033[m' * 40)

num = int(input('Digite um número: '))
print()
for c in range(1, 11):
    print(f'{num} x {c:^2} = {num * c}')

print('\n\033[34m@ebony_prog\033[m')

