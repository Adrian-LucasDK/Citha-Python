def ti (login, senha):
    return login == "admin" and senha =="admin"
    

while True:
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

    resul = ti(login, senha)
    print(resul)
    if resul:
        break
    