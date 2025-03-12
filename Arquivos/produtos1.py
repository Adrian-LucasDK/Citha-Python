import pandas as pd

dadosProdutos = pd.read_csv('produtos.csv')
print(dadosProdutos.columns)
dadosProdutos['preco'].max()
print("Médias de preços dos produtos: ", dadosProdutos['preco'].mean())