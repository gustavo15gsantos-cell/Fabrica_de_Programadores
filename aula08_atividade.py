contador = 0
while contador <3:
    contador = contador +1
    arquivo_de_nomes = open("arquivo de nomes.txt","a", encoding="utf-8")

    nomes = input("Digite 20 nomes:  \n")
    arquivo_de_nomes.write(f"{nomes}\n")


arquivo_de_nomes.close()
print("\n","-"*20, "\nArquivo criado com sucesso\n", "-"*20)