"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""
nome = 'Bruno'
print(nome, type(nome))
print('\n')

nome = 'Bruno Santana'
idade = 32  # int
altura = 1.82  # float
e_maior = idade > 18  # bool
peso = 90
imc = peso / (altura ** 2)

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print("É maior de idade:", e_maior)
print("IMC:", imc)
print('\n')

print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)

