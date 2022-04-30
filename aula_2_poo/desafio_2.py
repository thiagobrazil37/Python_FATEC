entrada_do_usuário = input("Digite uma letra: ")

if entrada_do_usuário in "aeiou":
    print("Vogal")
elif entrada_do_usuário in "1234567890":
    print("Há caracteres numéricos")
else:
    print("Consoante")   
    