import pywhatkit as kit
import pyautogui  # Adicionando a importação do pyautogui
import time

numero = input("Digite o número do WhatsApp (com DDI e DDD, sem espaços ou traços): ")
mensagem = input("Digite a mensagem que deseja enviar: ")

# Envia a mensagem
kit.sendwhatmsg_instantly(f"+{numero}", mensagem)

# Aguardar o tempo necessário para que o WhatsApp Web finalize o carregamento e digitação
time.sleep(3)  # Aguarda 3 segundos para que a mensagem seja digitada corretamente

# Agora, pressionamos Enter para enviar a mensagem
pyautogui.press("enter")

print("Mensagem enviada com sucesso!")
