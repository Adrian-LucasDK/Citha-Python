import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv('dados.csv')

# Converter as colunas 'produtividade' e 'agua' para valores numéricos, removendo 'kg' e 'l'
df['produtividade'] = df['produtividade'].str.replace('kg', '').astype(float)
df['agua'] = df['agua'].str.replace('l', '').astype(float)

# Calcular a produtividade média por tipo de produto
produtividade_media = df.groupby('tipo')['produtividade'].mean().round(2)

# Exibir a produtividade média por produto
print("Produtividade média por produto:")
print(produtividade_media.to_string(index=True))  # Utiliza to_string para formatar a saída sem o índice extra

# Encontrar o produto com maior produtividade média
produto_maior_produtividade = produtividade_media.idxmax()
maior_produtividade = produtividade_media.max()

# Exibir o produto com maior produtividade média
print(f'\nProduto com maior produtividade: {produto_maior_produtividade} ({maior_produtividade:.2f} kg)')

# Calcular o uso médio de água por tipo de produto
agua_media = df.groupby('tipo')['agua'].mean().round(2)

# Exibir o produto com menor uso médio de água
produto_menor_agua = agua_media.idxmin()
menor_agua = agua_media.min()

print(f'\nProduto com menor uso médio de água: {produto_menor_agua} ({menor_agua:.2f} litros)')

# Criar o gráfico de produtividade ao longo dos anos para cada produto
plt.figure(figsize=(10, 6))

# Para cada tipo de produto, plotar a produtividade ao longo do ano
for produto in df['tipo'].unique():
    dados_produto = df[df['tipo'] == produto]
    plt.plot(dados_produto['ano'], dados_produto['produtividade'], label=produto, marker='o')

# Adicionar título e rótulos aos eixos
plt.title('Produtividade ao longo do ano por produto')
plt.xlabel('Ano')
plt.ylabel('Produtividade (kg)')
plt.legend(title='Tipo de Produto')

# Exibir o gráfico
plt.grid(True)
plt.show()
