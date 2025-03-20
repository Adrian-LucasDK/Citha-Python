import csv
from collections import defaultdict
from plyer import notification
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from openpyxl import Workbook
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

def adicionar_dados(arquivo):
    with open(arquivo, 'a', newline='', encoding='utf-8') as csvfile:
        escritor = csv.writer(csvfile)
        while True:
            produto = input("Digite o nome do produto (ou 'sair' para finalizar): ")
            if produto.lower() == 'sair':
                break
            quantidade = input("Digite a quantidade vendida: ")
            preco = input("Digite o preço unitário: ")
            escritor.writerow([produto, quantidade, preco])

def ler_csv(arquivo):
    vendas = defaultdict(float)
    with open(arquivo, newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            produto = linha['Produto']
            quantidade = int(linha['Quantidade'])
            preco = float(linha['Preço'])
            vendas[produto] += quantidade * preco
    return vendas

def gerar_relatorio(vendas):
    if not vendas:
        print("Nenhum dado de vendas disponível para gerar relatório.")
        return

    produto_mais_vendido = max(vendas, key=vendas.get)
    total_geral = sum(vendas.values())

    print("Relatório de Vendas:")
    for produto, total in vendas.items():
        print(f"{produto}: R$ {total:.2f}")
    print(f"\nProduto mais vendido: {produto_mais_vendido} (R$ {vendas[produto_mais_vendido]:.2f})")
    print(f"Total geral de vendas: R$ {total_geral:.2f}")

    enviar_notificacao(produto_mais_vendido, total_geral)
    exibir_popup(produto_mais_vendido, total_geral)

def enviar_notificacao(produto_mais_vendido, total_geral):
    mensagem = f"Produto mais vendido: {produto_mais_vendido}\nTotal de vendas: R$ {total_geral:.2f}"
    notification.notify(
        title="Resumo de Vendas",
        message=mensagem,
        app_name="Sistema de Vendas"
    )

def exibir_popup(produto_mais_vendido, total_geral):
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    mensagem = f"Produto mais vendido: {produto_mais_vendido}\nTotal de vendas: R$ {total_geral:.2f}"
    messagebox.showinfo("Resumo de Vendas", mensagem)
    root.lift() # Trazer para o topo
    root.destroy()

def gerar_relatorio_excel(arquivo_csv, arquivo_excel):
    """
    Lê um arquivo CSV de vendas, agrupa os dados por produto e salva um relatório em Excel.

    Args:
        arquivo_csv (str): Caminho para o arquivo CSV de vendas.
        arquivo_excel (str): Caminho para o arquivo Excel de saída.
    """
    try:
        # Ler o arquivo CSV usando pandas
        df = pd.read_csv(arquivo_csv)

        # Agrupar os dados por produto e calcular o total de vendas
        relatorio = df.groupby('Produto')['Quantidade'].sum().reset_index()
        relatorio['Total'] = df.groupby('Produto').apply(lambda x: (x['Quantidade'] * x['Preço']).sum(), include_groups=False).reset_index(drop=True)

        # Criar um novo arquivo Excel
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Resumo"

        # Escrever o cabeçalho
        sheet.append(relatorio.columns.tolist())

        # Escrever os dados
        for index, row in relatorio.iterrows():
            sheet.append(row.tolist())

        # Salvar o arquivo Excel
        workbook.save(arquivo_excel)

        print(f"Relatório gerado com sucesso em {arquivo_excel}")

    except FileNotFoundError:
        print(f"Erro: Arquivo {arquivo_csv} não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def enviar_email(arquivo_excel, destinatario, remetente, senha):
    """
    Envia um e-mail com o relatório em Excel anexado.

    Args:
        arquivo_excel (str): Caminho para o arquivo Excel do relatório.
        destinatario (str): Endereço de e-mail do destinatário.
        remetente (str): Endereço de e-mail do remetente.
        senha (str): Senha do remetente.
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['To'] = destinatario
        msg['Subject'] = "Relatório de Vendas"

        body = "Segue em anexo o relatório de vendas."
        msg.attach(MIMEText(body, 'plain'))

        with open(arquivo_excel, "rb") as f:
            attach = MIMEApplication(f.read(), _subtype="xlsx")
            attach.add_header('Content-Disposition', 'attachment', filename=os.path.basename(arquivo_excel))
            msg.attach(attach)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server: #Alterar para o servidor de email desejado
            server.login(remetente, senha)
            server.send_message(msg)

        print("E-mail enviado com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro ao enviar o e-mail: {e}")

def obter_credenciais_email():
    """
    Cria uma janela para solicitar as credenciais de e-mail do usuário.

    Returns:
        tuple: Uma tupla contendo o e-mail do remetente, a senha e o e-mail do destinatário.
    """
    root = tk.Tk()
    root.title("Credenciais de E-mail")
    root.geometry("500x250")  # Aumenta o tamanho da janela
    root.attributes('-topmost', 1) # Janela sempre no topo

    remetente_label = tk.Label(root, text="Seu E-mail:")
    remetente_label.grid(row=0, column=0, padx=10, pady=10)
    remetente_entry = tk.Entry(root, width=40)  # Aumenta o tamanho do campo
    remetente_entry.grid(row=0, column=1, padx=10, pady=10)

    senha_label = tk.Label(root, text="Senha de Aplicativo:")
    senha_label.grid(row=1, column=0, padx=10, pady=10)
    senha_entry = tk.Entry(root, show="*", width=40)  # Aumenta o tamanho do campo
    senha_entry.grid(row=1, column=1, padx=10, pady=10)

    destinatario_label = tk.Label(root, text="E-mail do Destinatário:")
    destinatario_label.grid(row=2, column=0, padx=10, pady=10)
    destinatario_entry = tk.Entry(root, width=40)  # Aumenta o tamanho do campo
    destinatario_entry.grid(row=2, column=1, padx=10, pady=10)

    def enviar():
        root.quit()  # Encerra o loop principal, mas não destrói a janela

    enviar_button = tk.Button(root, text="Enviar", command=enviar)
    enviar_button.grid(row=3, column=1, padx=10, pady=10)

    root.mainloop()

    remetente = remetente_entry.get()
    senha = senha_entry.get()
    destinatario = destinatario_entry.get()

    root.destroy()  # Destrói a janela após obter os valores
    return remetente, senha, destinatario

if __name__ == "__main__":
    pasta_raiz = r"C:\Users\adria\Videos\Citha-Python\10 exercicios"
    arquivo_csv = os.path.join(pasta_raiz, "vendas.csv")
    arquivo_excel = os.path.join(pasta_raiz, "relatorio.xlsx")

    adicionar_dados(arquivo_csv)
    vendas = ler_csv(arquivo_csv)
    gerar_relatorio(vendas)
    gerar_relatorio_excel(arquivo_csv, arquivo_excel)

    # Obter credenciais de e-mail através da janela
    remetente, senha, destinatario = obter_credenciais_email()

    enviar_email(arquivo_excel, destinatario, remetente, senha)