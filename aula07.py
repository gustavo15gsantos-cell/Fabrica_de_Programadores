print(".--------- login ---------. \n") #cls linpa o play  #try:

lista_de_usuarios = ["vanessa","carla","enzo"]
lista_de_senha = ["van123","c4ely","en_z0"]

usuario = input("digite o seu usuário: \n")
senha = input("digite a sua senha: \n")

index_usuario = lista_de_usuarios.index(usuario)
index_senha = lista_de_senha.index(senha)

if index_usuario == index_senha:
    print("login bem sucedido!!!!")
else:
    print("usuário ou senha invalida !!!") 


    