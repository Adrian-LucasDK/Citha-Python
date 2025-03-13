import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados diretamente do arquivo CSV
dados = pd.read_csv(r'C:\Users\adria\Videos\Citha-Python\Arquivos\teste\dados.csv')

# Remover espaços extras nos nomes das colunas
dados.columns = dados.columns.str.strip()

# Exibir os dados
print(dados)
print("\n")

# Calcular o valor médio por tipo de item (Produto)
valor_medio = dados.groupby('Item')['Value'].mean().reset_index()

# Limitar o valor médio para 2 casas decimais
valor_medio['Value'] = valor_medio['Value'].round(2)

print("Valor médio por tipo de item:")
print(valor_medio)

# Encontrar o produto com maior valor
produto_max_valor = valor_medio.loc[valor_medio["Value"].idxmax()]

# Limitar o valor do produto máximo para 2 casas decimais
max_valor_formatado = round(produto_max_valor["Value"], 2)
print("\nProduto com maior valor:")
print(f"{produto_max_valor['Item']} - {max_valor_formatado}")

# Plotar o valor ao longo dos anos por país e produto
plt.figure(figsize=(12, 6))
sns.lineplot(data=dados, x="Year", y="Value", hue="Area", style="Item", markers=True)

# Ajustar o título e rótulos
plt.title("Valor ao longo dos anos por país e tipo de item")
plt.xlabel("Ano")
plt.ylabel("Valor")

# Ajustar a legenda para evitar que ela seja cortada
plt.legend(title="País e Produto", bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Exibir a grade
plt.grid(True)

# Ajustar o layout para não cortar a legenda
plt.tight_layout()

# Exibir o gráfico
plt.show()
