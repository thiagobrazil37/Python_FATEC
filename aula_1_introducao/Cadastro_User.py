#Abrir o arquivo (R - Ler, A = Sobrescrever, W = Escrever)

arquivo= open("db.csv","a")

arquivo.write(input("Animal: "))
              
arquivo.close()
