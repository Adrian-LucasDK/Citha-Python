import matplotlib.pyplot as plt
import pandas as pd

# Carregar os dados do arquivo CSV, especificando o delimitador ';'
caminho_arquivo = r'C:\Users\adria\Videos\Citha-Python\Dupla\dados3.csv'
dados = pd.read_csv(caminho_arquivo, delimiter=';')

# Extrair os dados das colunas
anos = dados['ano']
quantidades = dados['quantidade']

# Criando o gráfico de linha
plt.figure(figsize=(8, 5))
plt.plot(anos, quantidades, marker='o', linestyle='-', color='purple', label='Feminicídios')

# Adicionando títulos e rótulos
plt.title("Evolução da Taxa de Feminicídio no Brasil")
plt.xlabel("Ano")
plt.ylabel("Quantidade de Casos")
plt.xticks(anos)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Adicionando fontes como texto no gráfico
plt.figtext(0.5, 0.01, 'Fontes: www.congressoemfoco.com.br e www.g1.globo.com', ha='center', va='center', fontsize=10, color='gray')

# Exibir gráfico
plt.show()
