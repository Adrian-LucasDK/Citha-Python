def contar_vogais_em_arquivo():
    # Abre o arquivo 'texto.txt' no modo de leitura
    with open('texto.txt', 'r') as arquivo:
        conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo

    # Definindo as vogais
    vogais = "aeiouAEIOU"
    contador = 0
    
    # Contando as vogais no conteúdo
    for letra in conteudo:
        if letra in vogais:
            contador += 1
    
    return contador

# Chama a função e imprime o número de vogais
resultado = contar_vogais_em_arquivo()
print(f"O número de vogais no arquivo é: {resultado}")
