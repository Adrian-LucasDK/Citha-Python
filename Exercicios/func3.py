def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in texto:
        if char in vogais:
            contador += 1
    return contador

# Solicita ao usuário que insira uma palavra
palavra = input("Digite uma palavra: ")

# Chama a função e exibe o resultado
quantidade_vogais = contar_vogais(palavra)
print(f"A quantidade de vogais na palavra '{palavra}' é: {quantidade_vogais}")