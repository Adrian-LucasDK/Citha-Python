import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv(r'C:\Users\adria\Videos\Citha-Python\Arquivos\Dados Agricolas\dados.csv')

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

# Definir as cores para os produtos conhecidos (com cores mais distintas)
cores_produtos = {
    'Cebola': '#FFD700',  # Gold
    'Beterraba': '#DC143C',  # Crimson
    'Laranja': '#FFA500',  # Orange
    'Tomate': '#008000',  # Green
    'Batata': '#8B4513',  # SaddleBrown
    'Cenoura': '#800080',  # Purple
    'Maçã': '#FF6347',  # Tomato
    'Uva': '#6A5ACD',  # SlateBlue
    'Milho': '#00FFFF',  # Ciano
    'Morango': '#FF4500'  # OrangeRed
}

# Criar uma cor padrão para produtos desconhecidos
cor_padrao = '#808080'  # Gray

# Função para atribuir cores
def atribuir_cor(produto):
    return cores_produtos.get(produto, cor_padrao)

# Calcular a produtividade total por produto
produtividade_total = df.groupby('tipo')['produtividade'].sum()

# Obter as cores para cada produto
cores = [atribuir_cor(produto) for produto in produtividade_total.index]

# Criar o gráfico de pizza
plt.figure(figsize=(8, 8))

# Criar o gráfico de pizza
plt.pie(produtividade_total, labels=produtividade_total.index, colors=cores, autopct='%1.1f%%', startangle=90)

# Título do gráfico
plt.title('Produtividade Total por Produto')

# Exibir o gráfico
plt.axis('equal')  # Garantir que o gráfico seja desenhado como um círculo
plt.show()
