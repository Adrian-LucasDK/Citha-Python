n1 = int (input("Digite o primeiro número: "))
n2 = int (input("Digite o segundo número: "))

soma = n1 + n2

if soma > 20:
    print("Soma é maior que 20: ", soma)
    print("Nova valor: ", soma + 8)
else:
   print("Soma é menor que 20: ", soma)
   print("Nova valor: ", soma - 5)