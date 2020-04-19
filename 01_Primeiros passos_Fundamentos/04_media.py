''' Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''

# Resposta:

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))
nota4 = float(input('Digite a 4ª nota: '))
media = float((nota1 + nota2 + nota3 + nota4) / 4)
print(f'Média do aluno é: {media:.1f}')
