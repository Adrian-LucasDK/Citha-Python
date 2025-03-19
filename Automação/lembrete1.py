import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
import threading

# Função para exibir o lembrete
def mostrar_lembrete(mensagem):
    pyautogui.alert(text=mensagem, title="Lembrete", button="OK")

# Função para configurar o lembrete
def configurar_lembrete():
    try:
        # Pega a mensagem e o tempo em segundos
        mensagem = entrada_mensagem.get()
        tempo = int(entrada_tempo.get())

        # Verifica se a mensagem e o tempo são válidos
        if not mensagem:
            messagebox.showerror("Erro", "Por favor, insira uma mensagem.")
            return
        if tempo <= 0:
            messagebox.showerror("Erro", "Por favor, insira um tempo válido em segundos.")
            return

        # Desativa os campos e o botão de configuração para evitar múltiplos lembretes
        botao_configurar.config(state=tk.DISABLED)
        entrada_mensagem.config(state=tk.DISABLED)
        entrada_tempo.config(state=tk.DISABLED)

        # Exibe uma mensagem de confirmação
        messagebox.showinfo("Lembrete Configurado", f"Lembrete configurado para {tempo} segundos.")

        # Usando thread para não bloquear a interface gráfica
        threading.Thread(target=esperar_e_mostrar, args=(tempo, mensagem)).start()

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido para o tempo.")

# Função para esperar o tempo e exibir o lembrete
def esperar_e_mostrar(tempo, mensagem):
    time.sleep(tempo)  # Espera o tempo (em segundos)
    mostrar_lembrete(mensagem)

# Criando a janela principal
janela = tk.Tk()
janela.title("Lembrete")

# Configurando a interface gráfica
label_mensagem = tk.Label(janela, text="Digite a mensagem do lembrete:")
label_mensagem.pack(pady=10)

entrada_mensagem = tk.Entry(janela, width=40)
entrada_mensagem.pack(pady=5)

label_tempo = tk.Label(janela, text="Digite o tempo (em segundos):")
label_tempo.pack(pady=10)

entrada_tempo = tk.Entry(janela, width=10)
entrada_tempo.pack(pady=5)

botao_configurar = tk.Button(janela, text="Configurar Lembrete", command=configurar_lembrete)
botao_configurar.pack(pady=20)

# Inicia a janela
janela.mainloop()
