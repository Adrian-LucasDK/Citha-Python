import pyautogui
import time

def enviar_mensagem(mensagem):
    time.sleep(3)  # Tempo para o usuário alternar para o WhatsApp Web
    pyautogui.typewrite(mensagem)
    pyautogui.press("enter")

def menu():
    print("Escolha o tipo de mensagem:")
    print("1 - Mensagem personalizada")
    print("2 - Mensagem de bom dia")
    print("3 - Mensagem motivacional")
    print("4 - Mensagem de lembrete")
    print("5 - Mensagem Especial")

    escolha = input("Digite o número da opção: ")

    if escolha == "1":
        mensagem = input("Digite sua mensagem personalizada: ")
    elif escolha == "2":
        mensagem = "Bom dia! Espero que tenha um ótimo dia! ☀️"
    elif escolha == "3":
        mensagem = "Nunca desista dos seus sonhos. Cada passo te aproxima mais do sucesso! 🚀"
    elif escolha == "4":
        mensagem = "Não se esqueça da reunião hoje às 15h! 📅"
    elif escolha == "5":
        mensagem = "Você é especial e eu gosto de vc"
    else:
        print("Opção inválida. Escolhendo mensagem padrão.")
        mensagem = "Olá! Esta é uma mensagem automática."

    return mensagem

if __name__ == "__main__":
    mensagem_escolhida = menu()
    print("Você tem 3 segundos para alternar para o WhatsApp Web...")
    enviar_mensagem(mensagem_escolhida)
    print("Mensagem enviada com sucesso!")
