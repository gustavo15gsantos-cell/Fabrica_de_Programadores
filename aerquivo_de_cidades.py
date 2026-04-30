contador = 0
while contador <20:
    contador = contador +1
    arquivo_de_cidades = open("arquivo de cidades.txt","a", encoding="utf-8")

    nomes = input("Digite 20 nomes:  \n")
    arquivo_de_cidades.write(f"{nomes}\n")


arquivo_de_cidades.close()
print("\n","-"*20, "\nArquivo criado com sucesso\n", "-"*20)