''' Progressão aritmética '''

# Resposta:
from time import sleep

print('_' * 70)
print('{:^78}'.format('\033[34mPROGRESSÃO ARITMÉTICA\033[m'))
print('º' * 70)

sair = ''

while not sair == 'S':
    prim_termo = int(input('Digite o primeiro termo: '))
    razao = int(input('Digite a razão: '))
    qtd_termo = int(input('Quantos termos quer mostrar: '))
    dec = prim_termo + (qtd_termo - 1) * razao
    print('_' * (qtd_termo * 6 + 3))

    for c in range(prim_termo, dec + razao, razao):
        print(f'{c} ', end='-> ')
    print('\033[32mFim.\033[m')
    print('º' * (qtd_termo * 6 + 3))
    sair = str(input('\nTecle \033[34mS para sair.\033[m ou '
                     '\033[31mN para nova progressão\033[m: ')).strip().upper()
    print('º' * 70)
    if sair == 'S':
        print('\n\n')
        break
    elif sair != 'N':
        print('\033[31mDado Inválido!\033[m Aguarde, sistema sendo encerrado!')
        break
sleep(1)
print('_' * 70)
sleep(0.5)
print('{:^78}'.format('\033[35mObrigado por utilizar o sistema!\033[m'))
sleep(0.5)
print('{:^78}'.format('\033[m@ebony_prog\033[m'))
sleep(0.5)
print('º' * 70)
