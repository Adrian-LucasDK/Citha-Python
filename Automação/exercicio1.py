import time

def obter_nomes():
    nomes = input("Digite os nomes separados por vírgula: ").split(',')
    return [nome.strip() for nome in nomes]

def criar_mensagem(nome):
    return f"Olá, {nome}! Espero que você esteja tendo um ótimo dia! 😊"

def enviar_mensagens(nomes):
    for nome in nomes:
        mensagem = criar_mensagem(nome)
        print(mensagem)
        time.sleep(1.5)  # Simula um pequeno atraso entre as mensagens

def main():
    print("Bem-vindo ao Chatbot de Mensagens Personalizadas!")
    nomes = obter_nomes()
    enviar_mensagens(nomes)
    print("Mensagens enviadas com sucesso!")

if __name__ == "__main__":
    main()