"""
+, -, *, /, //, **, %, ()
"""
print('Multiplicação * ', 10 * 10)
print('Adição + ', 10 + 10)
print('Subtração - ', 10 - 5)
print('Divisão / ', 10 / 2)
print('\n')

# Não se pode multiplicar 2 tipos string, mas se 1 for um inteiro com outro string pode.
# No caso de multiplicar inteiro com string, o * (operador de multiplicação) vai funcionar como op de multiplicação.
print(10 * '10')
print('A' * 10)
print('\n')

# Não pode usar o + pra concatenar um string e um inteiro.
# Ou usa o + pra somar int/float ou pra concatenar strings.
print(10 + 20)
print(7.5 + 2.5)
print('Bruno' + ' ' + 'Aarão' + ' ' + 'Santana')
print('\n')

# "//" retorna a divisão inteira
print(10.5 // 3)

# "**" retorna a exponenciação
print(2 ** 3)

# "%" retorna o módulo (o resto da divisão)
print(10.5 % 3)
print('\n')

# Os parênteses alteram a precedência dos operadores
print(5 + 2 * 10)  # O resultado será 25, pois "*" precede a "+"
print((5 + 2) * 10)  # O resultado será 70, pois o "()" mudou a precedência
print('\n')

print('Fim da aula 5.')
