#revisão

#o que são variaveis?
#a = 10
#b = 20

#print(a+b)

#pergunta 01

#lista = ["vanessão","carlota","enzo do pix"]

#x = input("digite seu nome:\n")

#if x in lista:
#    print("seu nome esta na lista.....")

#else:
#    print("seu nome não esta na lista!!!!!!!!")




#========================================================================================================
#pergunta 02

#idade = int(input("digite sua idade para votar\n"))

#if idade >=16:
#   print("você pode votar. ")

#else :
#   print("você não pode votar !!!!!!!!")



#===========================================================================================================
#pergunta 03 

#minha_garagem = ["bmw","mercedes-bens","audi","aston martin"]
#preco = [35000, 40000, 20000,80000]

estoque = ["chevy","fiat","peugeot","VolksWagem","lexus","ferrari",]
preco_loja = [1000,500,1.99,20000,60000,90000]

loja_barato = []  # abaixo de 20 mil
loja_caro = []    # acima de 20 mil


i = 0 
for preco in preco_loja:
    if preco >=20000:
        loja_caro.append(estoque[i])
else:
        loja_barato.append(estoque[i])
i = i +1