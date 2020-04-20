''' Faça um programa que leia e valide as seguintes informações:
        a. Nome: maior que 3 caracteres;
        b. Idade: entre 0 e 150;
        c. Salário: maior que zero;
        d. Sexo: 'f' ou 'm';
        e. Estado Civil: 's', 'c', 'v', 'd'; '''

# Resposta:

while True:
    nome = input('NOME: ').strip().title()
    if len(nome) <= 3:
        print('\033[31mDado inválido!\033[m')
    else:
        while True:
            idade = int(input('IDADE: '))
            if idade < 0 or idade > 150:
                print('\033[31mDado inválido!\033[m')
            else:
                while True:
                    salario = float(input('SALÁRIO: '))
                    if salario <= 0:
                        print('\033[31mDado inválido!\033[m')
                    else:
                        while True:
                            sexo = input('SEXO (F / M): ').strip().upper()
                            if sexo not in 'MF':
                                print('\033[31mDado inválido!\033[m')
                            else:
                                if sexo == 'F':
                                    sexo = 'Feminino'
                                else:
                                    sexo = 'Masculino'
                                while True:
                                    print('''Tecle:
   [ S ] Solteiro(a)
   [ C ] Casado(a)
   [ V ] Viúvo(a)
   [ D ] Divorciado(a)''')
                                    estado = input('ESTADO CIVIL: ').strip().upper()
                                    if estado not in 'SCVD':
                                        print('\033[31mDado inválido!\033[m')
                                    else:
                                        if estado == 'S':
                                            estado = 'Solteiro(a)'
                                        elif estado == 'C':
                                            estado = 'Casado(a)'
                                        elif estado == 'V':
                                            estado = 'Viúvo(a)'
                                        else:
                                            estado = 'Divorciado(a)'
                                        break
                                break
                        break
                break
        break

print()
print('\033[32m*\033[m' * 50, F'\nNOME: {nome}.\nIDADE: {idade} anos.\nSALÁRIO: R${salario:.2f}\n'
                              F'SEXO: {sexo}\nESTADO CIVIL: {estado}.')

print('\n\n\033[34m@ebony_prog\033[m')
