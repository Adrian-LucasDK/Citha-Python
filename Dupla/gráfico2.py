import matplotlib.pyplot as plt
import pandas as pd

# Carregar os dados do arquivo CSV
caminho_arquivo = r"C:\Users\adria\Videos\Citha-Python\Dupla\dados2.csv"
dados = pd.read_csv(caminho_arquivo, delimiter=';')

# Extraindo categorias e quantidades
categorias = dados['Tipos'].tolist()
quantidades = dados['Quantidade'].tolist()

# Criando o gráfico de pizza
plt.figure(figsize=(8, 5))
plt.pie(quantidades, labels=categorias, autopct='%1.1f%%', colors=["red", "purple"], startangle=90, shadow=True)

# Adicionando título
plt.title("Distribuição de Homicídios e Feminicídios no Brasil (2024)")

# Exibir gráfico
plt.show()