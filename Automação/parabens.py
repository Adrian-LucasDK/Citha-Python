import time
import pyautogui
import subprocess

def selecionar_mensagem():
    mensagens = {
        1: "Olá! Como você está?",
        2: "Bom dia! Tenha um ótimo dia!",
        3: "Ei, lembra daquele nosso projeto? Precisamos conversar!",
        4: "Mensagem personalizada"
    }
    
    print("Escolha uma mensagem para enviar:")
    for key, value in mensagens.items():
        print(f"{key}: {value}")
    
    escolha = int(input("Digite o número da mensagem desejada: "))
    
    if escolha == 4:
        return input("Digite sua mensagem personalizada: ")
    return mensagens.get(escolha, "Olá! Como você está?")

def abrir_word_e_digitar(mensagem):
    try:
        # Abrir o Microsoft Word (ajuste o caminho conforme necessário)
        subprocess.Popen(["start", "winword"], shell=True)
        time.sleep(5)  # Aguarda o Word abrir completamente
        
        # Selecionar o modelo em branco pressionando o atalho 'Ctrl + N'
        pyautogui.hotkey('ctrl', 'n')
        time.sleep(3)  # Aguarda o novo documento ser carregado
        
        # Se o foco não estiver no documento, clicamos na área do corpo do documento
        pyautogui.click(300, 300)  # Clica no corpo do documento para garantir que o foco esteja lá
        
        # Digitar a mensagem no documento
        pyautogui.write(mensagem)
        pyautogui.press('enter')  # Pressiona Enter para garantir que a mensagem seja registrada
        print("Mensagem digitada no Word com sucesso!")
    except Exception as e:
        print(f"Erro ao abrir o Word ou digitar a mensagem: {e}")

def main():
    # Escolher a mensagem
    mensagem = selecionar_mensagem()

    # Abrir o Word e digitar a mensagem
    abrir_word_e_digitar(mensagem)

if __name__ == "__main__":
    main()
