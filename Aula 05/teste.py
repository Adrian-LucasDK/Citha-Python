nome = str (input("Digite o seu nome: "))
cpf = int (input("Digite seu cpf: "))

matriculado = (cpf == 123)

if matriculado:
    print(f"{nome} você está matriculado")
else:
    print(f"{nome} você não está matriculado")

print (type(cpf))