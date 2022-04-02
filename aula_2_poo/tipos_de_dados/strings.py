import string

# aspas duplas
"Todos os sapos pulam os rios"

# aspas simples
'nem todos os rios são quentes'

# aspas triplas duplas: permite quebra de linha
"""mas todos os quentes são rios"""

# aspas triplas simples: permite quebra de linha
'''e todos os sapos são anfíbios.'''


# string por função
#input("Digite seu nome: ")

# solicitando dados do usuário
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# print(f"Olá, {nome}. Você tem {idade} anos")

print(f"Olá, {nome.title()}. Você tem {idade} anos")