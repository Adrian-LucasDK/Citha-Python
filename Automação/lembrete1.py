import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
import threading

# Lista para armazenar os lembretes
lembretes = []

# Função para exibir o lembrete
def mostrar_lembrete(mensagem):
    pyautogui.alert(text=mensagem, title="Lembrete", button="OK")

# Função para esperar o tempo e exibir o lembrete
def esperar_e_mostrar(tempo, mensagem, repeticoes=1, intervalo=0):
    for i in range(repeticoes):
        time.sleep(tempo if i == 0 else intervalo)  # Espera o tempo inicial na 1ª vez, depois segue o intervalo
        mostrar_lembrete(mensagem)

# Função para adicionar um novo lembrete
def adicionar_lembrete():
    try:
        mensagem = entrada_mensagem.get()
        tempo = int(entrada_tempo.get())
        repetir = var_repetir.get()
        repeticoes = int(entrada_repeticoes.get()) if repetir else 1
        intervalo = int(entrada_intervalo.get()) if repetir else 0

        if not mensagem:
            messagebox.showerror("Erro", "Por favor, insira uma mensagem.")
            return
        if tempo <= 0 or (repetir and (repeticoes <= 0 or intervalo <= 0)):
            messagebox.showerror("Erro", "Por favor, insira valores válidos para tempo e repetições.")
            return

        # Adiciona o lembrete à lista
        lembretes.append((tempo, mensagem, repeticoes, intervalo))

        # Atualiza a lista de lembretes na interface
        tipo_lembrete = "Recorrente" if repetir else "Único"
        lista_lembretes.insert(tk.END, f"{mensagem} - {tipo_lembrete} - {tempo}s {'a cada ' + str(intervalo) + 's, ' + str(repeticoes) + 'x' if repetir else ''}")

        # Limpa os campos de entrada
        entrada_mensagem.delete(0, tk.END)
        entrada_tempo.delete(0, tk.END)
        entrada_repeticoes.delete(0, tk.END)
        entrada_intervalo.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos para o tempo e repetições.")

# Função para iniciar os lembretes configurados
def iniciar_lembretes():
    if not lembretes:
        messagebox.showerror("Erro", "Nenhum lembrete adicionado.")
        return

    messagebox.showinfo("Lembretes Iniciados", "Os lembretes foram iniciados.")

    # Criando uma thread para cada lembrete
    for tempo, mensagem, repeticoes, intervalo in lembretes:
        threading.Thread(target=esperar_e_mostrar, args=(tempo, mensagem, repeticoes, intervalo)).start()

    # Limpa a lista de lembretes depois de iniciar
    lembretes.clear()
    lista_lembretes.delete(0, tk.END)

# Criando a janela principal
janela = tk.Tk()
janela.title("Lembretes")

# Configurando a interface gráfica
label_mensagem = tk.Label(janela, text="Digite a mensagem do lembrete:")
label_mensagem.pack(pady=5)

entrada_mensagem = tk.Entry(janela, width=40)
entrada_mensagem.pack(pady=5)

label_tempo = tk.Label(janela, text="Digite o tempo inicial (em segundos):")
label_tempo.pack(pady=5)

entrada_tempo = tk.Entry(janela, width=10)
entrada_tempo.pack(pady=5)

# Opção para repetir o lembrete
var_repetir = tk.BooleanVar()
check_repetir = tk.Checkbutton(janela, text="Repetir várias vezes", variable=var_repetir)
check_repetir.pack(pady=5)

# Campos para definir o intervalo e quantas vezes repetir
label_repeticoes = tk.Label(janela, text="Quantas vezes repetir:")
label_repeticoes.pack(pady=2)

entrada_repeticoes = tk.Entry(janela, width=10)
entrada_repeticoes.pack(pady=2)

label_intervalo = tk.Label(janela, text="Intervalo entre repetições (em segundos):")
label_intervalo.pack(pady=2)

entrada_intervalo = tk.Entry(janela, width=10)
entrada_intervalo.pack(pady=2)

botao_adicionar = tk.Button(janela, text="Adicionar Lembrete", command=adicionar_lembrete)
botao_adicionar.pack(pady=5)

# Lista de lembretes adicionados
label_lista = tk.Label(janela, text="Lembretes adicionados:")
label_lista.pack(pady=5)

lista_lembretes = tk.Listbox(janela, width=60, height=5)
lista_lembretes.pack(pady=5)

botao_iniciar = tk.Button(janela, text="Iniciar Lembretes", command=iniciar_lembretes)
botao_iniciar.pack(pady=10)

# Inicia a janela
janela.mainloop()
