lista = ["Vanessa" , "Carla" , "Enzo" , "Gustavo"]

contador = 0
while contador <4:
    contador = contador +1

    lista_nomes = lista

    x = input("digite nomes:\n")

    lista_nomes.append(x)

print(f"{lista}")
print(" Nomes acrecentado com sucesso!!!!!!! ")