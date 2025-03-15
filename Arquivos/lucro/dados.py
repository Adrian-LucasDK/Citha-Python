import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Carregar os dados diretamente do arquivo CSV
df = pd.read_csv(r'C:\Users\adria\Videos\Citha-Python\Arquivos\lucro\dados.csv')

# Calcular o lucro (Vendas * Custo_medio)
df['Lucro'] = df['Vendas'] * df['Custo_medio']

# Calcular a rentabilidade como lucro por quilo produzido (Lucro / Produção)
df['Rentabilidade'] = df['Lucro'] / df['Producao']

# Exibir os dados com as novas colunas
print("Dados com rentabilidade calculada:")
print(df)

# Encontrar o cultivo mais rentável
cultivo_mais_rentavel = df.loc[df['Rentabilidade'].idxmax()]

print("\nCultivo mais rentável:")
print(f"{cultivo_mais_rentavel['Peixes']} - Rentabilidade: {cultivo_mais_rentavel['Rentabilidade']:.2f}")

# Plotar a rentabilidade de cada peixe
plt.figure(figsize=(8, 5))
sns.barplot(x='Peixes', y='Rentabilidade', data=df, palette='viridis')

# Ajustar título e rótulos
plt.title("Rentabilidade dos Cultivos de Peixes")
plt.xlabel("Tipo de Peixe")
plt.ylabel("Rentabilidade (Lucro por quilo)")

# Exibir o gráfico
plt.tight_layout()
plt.show()
