''' Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário informe um valor válido. '''


# Resposta:

while True:
    nota = float(input('Digite uma nota entre 0 e 10: '))
    if nota > 10:
        print('\033[31mDado inválido!\033[m')
    else:
        print('\033[32mNota cadastrada com sucesso!\033[m')
        break

print('\n\n\033[34m@ebony_prog\033[m')