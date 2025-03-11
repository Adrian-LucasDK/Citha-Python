import pandas as pd 

dadosProdutos = pd.read_csv(r"C:\Users\adria\Videos\Citha-Python\Aula 07\Biblioteca\Produtos.csv", names=['Produtos', 'PRECO'], skiprows=1 )
dadosProdutos['PRECO'].max()
dadosProdutos['PRECO'].min()
print("Média de Preço dos Produtos: ", dadosProdutos['PRECO'].mean())