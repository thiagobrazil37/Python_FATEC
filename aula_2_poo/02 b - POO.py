class Balde:
    "Essa classe representa os cachorros e suas espécies que estão cadastradas em nosso sistema"

    def __init__(self):

        self.marca = ""
        self.durabilidade = 0
        self.volume = ""
        self.porte = ""


    def __str__(self):
        return self.marca
#
#     def __repr__(self):
#         return self.marca

# instanciamento
castelo_1 = Balde()
castelo_2 = Balde()

# ^^^^^    =  ^^^^^^
# |||||    =  ||||||
# Objeto   =  Molde

print(castelo_1)
print(castelo_2)
