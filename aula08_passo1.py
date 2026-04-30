
 
arquivo = open("arquivo.txt" ,"a" ,encoding="utf-8")

nome = input("digite seu nome: \n")
nota = int(input("digite sua nota: \n"))

arquivo.write("-"*20)
arquivo.write("\n Boletim \n")

arquivo.write("-"*20)

arquivo.write(f"\n Aluno: {nome}\n")
arquivo.write(f"\n Nota: {nota}\n")
arquivo.write("-"*20)


arquivo.close() 