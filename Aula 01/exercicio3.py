#Autor: Adrian Lucas Souza da Silva

# while para que quando o usuário digitar um número negativo, o programa peça para digitar novamente
while True:

    # input dos números
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    # soma dos números
    soma = n1 + n2

    # condição para a soma
    if soma > 20 and n1 >= 0 and n2 >= 0:
        print("Soma é maior que 20: ", soma)
        print("Nova valor: ", soma + 8)
        break
    elif soma <= 20 and n1 >= 0 and n2 >= 0:
        print("Soma é menor que 20: ", soma)
        print("Nova valor: ", soma - 5)
        break
    else:
        print(
        "Infelizmente você digitou um número negativo e não foi possivel realizar a soma")
