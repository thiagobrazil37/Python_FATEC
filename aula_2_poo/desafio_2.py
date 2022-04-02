
from itertools import count
from operator import countOf


entrada_do_usuário = input("Digite uma letra: ")

if entrada_do_usuário in "aeiou":
    print("Vogal")
else:
    print("Consoante")