"""
Entrada de dados
função input: serve para entrada de dados. O usuário vai digitar e vai para uma variável.
Tudo o que o usuário digitar no input será lido como str, mesmo que sejam números:
    nome = input("Qual é o seu nome? ")
    print(f'O usuário digitou {nome} e o tipo da variável é ' f'{type(nome)}')
Pode usar o cast para mudar o tipo da variável:
    idade = input('Qual a sua idade? ')
    ano_nascimento = 2022 - idade
    *** Isso vai dar certo? Não, pois idade será lido como str na função input
    *** O que fazer? Usar o cast para mudar o tipo de variável:
    ano_nascimento = 2022 - int(idade)
"""
nome = input("Qual é o seu nome? ")
idade = input('Qual a sua idade? ')
ano_nascimento = 2022 - int(idade)
print()
print(f'{nome} tem {idade} anos.')
print(f'{nome} nasceu em {ano_nascimento}.')
print()

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')
print(numero_1 + numero_2)
# A função input lerá como str. Ao invés de somar, vai concatenar as "str".
print()

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
print(numero_1 + numero_2)
# Agora, com str se transformando em int, será feita a soma
