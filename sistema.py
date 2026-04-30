#crie um sistema que atravez de uma lista de nomes e lista de senhas verifique que o usuario digitado esta na lista e que a senha coresponda a index do usuario. 
print("<|------------- login de lista ------------|>\n")


lista_de_usuarios = ["Hebert","Léo","Gustavo"]
lista_de_senha = ["vanessa_amor",123,"Gustav0"]

usuario = input("digite o seu usuário: \n")
senha = int(input("digite a sua senha: \n"))

index_usuario = lista_de_usuarios.index(usuario)
index_senha = lista_de_senha.index(senha)

if index_usuario == index_senha:
    print("login bem sucedido!!!!")
else:
    print("usuário ou senha invalida !!!") 