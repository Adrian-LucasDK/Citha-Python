def maior(lista):
    if not lista:
        return None
    maior_valor = lista[0]
    for numero in lista:
        if numero > maior_valor:
            maior_valor = numero
    return maior_valor

# Solicita ao usuário para digitar os números
numeros = []
quantidade = int(input("Quantos números você deseja inserir? "))

for _ in range(quantidade):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print("O maior número é:", maior(numeros))