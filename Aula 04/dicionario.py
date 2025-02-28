# Dicionário produto
produto = {
    'Nome:': ['Notebook', 'Notebook', 'Notebook', 'Notebook', 'Notebook'], 
    'Marca:': ['Dell', 'Lenovo', 'Samsung', 'Asus', 'Acer'],
    'Preço:': [4500.00, 3500.00, 2500.00, 1500.00, 500.00],
    'Quantidade:': [10, 20, 30, 40, 50],
}

#Adicione uma outra chave com valores
produto['Cor:'] = ['Preto', 'Prata', 'Cinza', 'Azul', 'Vermelho']


 # Acessando os valores do dicionário
nome = produto['Nome:']
marca = produto['Marca:']
preco = produto['Preço:']
quantidade = produto['Quantidade:']
cor = produto['Cor:']


# Imprimindo uma quebra de linha
print("\n")

# Imprimindo os valores
for chave, valor in produto.items():
    print(chave, valor)

# Alterando o valor de um item do dicionário
#produto['Marca:'] = 'Lenovo'

# Imprimindo uma quebra de linha
print("\n")

# Acessando os valores do dicionário
nome = produto['Nome:']
marca = produto['Marca:']
preco = produto['Preço:']
quantidade = produto['Quantidade:']
cor = produto['Cor:']


# Imprimindo os valores
for chave, valor in produto.items():
    print(chave, valor)

# Imprimindo uma quebra de linha
print("\n")

# Imprimindo os valores do dicionário com zip e for
for nome, marca, preco, quantidade, cor in zip(produto['Nome:'], produto['Marca:'], produto['Preço:'], produto['Quantidade:'], produto['Cor:']):
    print('Nome:', nome, 'Marca:', marca, 'Preço:', preco, 'Quantidade:', quantidade, 'Cor:', cor)


# Imprimindo uma quebra de linha
print("\n")