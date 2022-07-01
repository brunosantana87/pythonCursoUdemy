'''
# print(123456)
# print('Bruno', 'Santana')

print('Bruno', 'Santana', sep='-', end='#####')
print('João', 'e', 'Maria', sep='-', end='')

sep: utilizado como separador na função print
end: utilizado ao final. Pode ser utilizado para evitar a quebra de linha automática, ligando 2 ou mais funções print.
'''

'''
931.959.180-64
cpf aleatório para exercício envolvendo sep e end
'''
print('931', '959', '180', sep='.', end='-')
print('64')

# E essa foi a aula 2.

'''
Pergunta 1:
Qual a saída do comando abaixo:

print('Estou', 'aprendendo', 'Python', sep='-', end=' ')
print('isso é muito', 'legal', sep='-', end='')

Resposta:
Estou-aprendendo-Python isso é muito-legal
'''

print('Estou', 'aprendendo', 'Python', sep='-', end=' ')
print('isso é muito', 'legal', sep='-')

print('Esse é o fim da aula! Até a próxima!')
