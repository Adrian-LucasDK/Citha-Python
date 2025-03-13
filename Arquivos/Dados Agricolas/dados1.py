import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar pandas para exibir todos os dados
pd.set_option('display.max_rows', None)  # Mostrar todas as linhas
pd.set_option('display.max_columns', None)  # Mostrar todas as colunas
pd.set_option('display.width', None)  # Ajustar largura para exibição completa
pd.set_option('display.max_colwidth', None)  # Exibir texto completo nas colunas

# Carregar os dados
dados = pd.read_csv(r'C:\Users\adria\Videos\Citha-Python\Arquivos\Dados Agricolas\dados.csv')

# Remover espaços extras nos nomes das colunas
dados.columns = dados.columns.str.strip()

# Limpar as colunas 'produtividade' e 'agua', removendo as unidades e convertendo para números
dados['produtividade'] = dados['produtividade'].str.replace('kg', '').astype(float)
dados['agua'] = dados['agua'].str.replace('l', '').astype(float)

# Exibir todos os dados
print(dados)
print("\n")

# Calcular a produtividade média por tipo de cultivo
produtividade_media = dados.groupby('tipo')['produtividade'].mean().reset_index()
print(produtividade_media)


# Encontrar o produto com maior produtividade
produto_max_produtividade = produtividade_media.loc[produtividade_media["produtividade"].idxmax()]
print("\nProduto com maior produtividade: ")
print(f"{produto_max_produtividade['tipo']} - {produto_max_produtividade['produtividade']} kg")


# Calcular o uso médio de água por tipo de cultivo
uso_agua_medio = dados.groupby("tipo")["agua"].mean()
produto_min_uso_agua = uso_agua_medio.idxmin()
print("\nProduto com menor uso médio de água:", produto_min_uso_agua)

# Plotar a produtividade ao longo dos anos por tipo de cultivo
plt.figure(figsize=(10,6))
sns.lineplot(data=dados, x="ano", y="produtividade", hue="tipo", marker="o")

plt.title("Produtividade ao longo dos anos por tipo de cultivo")
plt.xlabel("Ano")
plt.ylabel("Produtividade (Toneladas por Hectare)")
plt.legend(title="Tipo de Cultivo")
plt.grid(True)
plt.show()
