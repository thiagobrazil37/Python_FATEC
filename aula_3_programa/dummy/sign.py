# author: thiago braz
# version: 1.0.0
# date: apr/2022
# description: este programa cadastra novos usuários
# name: sign

from hashlib import	sha256
import sys
from time import sleep

# mensagem de boas vindas ao usuário
message = "Seja bem-vindo ao Sign: Sistema Integrado de Gestão de Nomes! Selecione uma das opções abaixo: "

# imprimindo a mensagem de boas vindas ao usuário
for letter in message:
    sys.stdout.write(letter)
    sys.stdout.flush()
    sleep (0.020)
print()
    
# setando as opções do menu    
opcoes_menu = ["Cadastrar","Acessar","Esqueci minha senha", "Fale conosco"]

# imprimindo menu de opções
count = 1
for opcao in opcoes_menu:
    print(f"{count} - {opcao}")
    count += 1 #count = count +1
    

opcao_selecionada = int(input("Qual a opção desejada? "))

with open("c:/Users/FatecSdP-TI/Documents/Python_FATEC/aula_3_programa/dummy/sign/db.csv","w") as arquivo:
    arquivo.write("test")
    