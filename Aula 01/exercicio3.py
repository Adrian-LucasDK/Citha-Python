while True:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    soma = n1 + n2

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
