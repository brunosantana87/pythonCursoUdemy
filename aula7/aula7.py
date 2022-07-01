nome = 'Bruno Santana'
idade = 32  # int
altura = 1.82  # float
e_maior = idade > 18  # bool
peso = 90
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)

# Utilizar "f strings". Ao usar não precisa se preocupar com o tipo.
# Para limitar as casas decimais colocar, p. ex., ":.2f" (2 = casas decimais/ f vem de float)

print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')

# Função format: {} para variáveis; no final da str colocar ".format(var1, var2, etc)"
# OBS: para limitar as casas decimais, colocar o ":.2f" (ex: 2 casas dec) dentro do {}
# Pode atribuir números as variáveis (0, 1, 2, etc), colocar dentro do {} e repetir se quiser

print('{} tem {} anos de idade e seu IMC é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos de idade e seu IMC é {2:.2f}. {0} está com sobrepeso, pois {2:.2f} se encontra acima de 25.'.format(nome, idade, imc))

# Pode usar os parâmetros nomeados dentro das chaves
print('{n} tem {i} anos de idade e seu IMC é {p:.2f}'.format(n=nome, i=idade, p=imc))
