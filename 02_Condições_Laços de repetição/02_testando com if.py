''' Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações. '''

# Resposta:

while True:
    usuario = input('Usuário: ').lower()
    senha = input('Senha: ').lower()

    if senha == usuario:
        print('\033[31mSenha não pode ser igual ao usuário.\033[m')
    else:
        print('\033[33mUsuário cadastrado com sucesso.\033[m')
        break

print('\n\n\033[34m@ebony_prog\033[m')