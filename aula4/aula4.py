"""
Tipos de dados
str - string - textos 'Assim' "Assim"
int - inteiro - 123456, 0, -10, -50, -60, -1500, 1500
float - real/ponto flutuante - 10.50, 1.5, -10.10, 0.0
bool - booleano/lógico - True/False; 10 == 10
"""
print('Bruno')
print('Bruno', type('Bruno'))
print(10, type(10))
print(25.237, type(25.237))
print(10 == 10, type(10 == 10))
# Como fazer um type casting (correção de tipo):
print('10', type('10'), type((int('10'))))
# No caso, converteu a o '10' de str pra int na última parte
print(10 + 10)  # Soma de 2 números int
print('10' + '10')  # Concatenação de 2 str
print('Bru' + 'no', '\n')  # Idem o de cima

# Nome: str
print('Bruno', type('Bruno'))

# Idade: int
print(34, type(34))

# Altura: float
print(1.82, type(1.82))

# É maior de idade
print(34 > 18, type(34 > 18))

print('Fim da aula 4.')
