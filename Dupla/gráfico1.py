import matplotlib.pyplot as plt
import pandas as pd

# Caminho do arquivo CSV
caminho_arquivo = r'C:\Users\adria\Videos\Citha-Python\Dupla\dados.csv'

# Ler o arquivo CSV usando pandas
try:
    df = pd.read_csv(caminho_arquivo, sep=';')
except FileNotFoundError:
    print(f"Erro: Arquivo não encontrado em {caminho_arquivo}")
    exit()

# Cores para os gráficos
cores = ['skyblue', 'salmon', 'lightgreen', 'gold']

# Criar gráficos de pizza lado a lado
fig, axs = plt.subplots(1, 2, figsize=(16, 8))  # 1 linha, 2 colunas

for i, ano in enumerate([2024, 2025]):
    dados_ano = df[df['Ano'] == ano]
    tipos = dados_ano['Tipos'].tolist()
    quantidades = dados_ano['Quantidade'].tolist()

    axs[i].pie(quantidades, labels=tipos, colors=cores, autopct='%1.1f%%', startangle=140)
    axs[i].set_title(f'Taxa de Crimes no Amazonas - {ano}')
    axs[i].axis('equal')

plt.show()