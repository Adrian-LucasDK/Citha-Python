def criar_mensagem_personalizada():
  mensagem = input("Digite sua mensagem personalizada: ")
  return mensagem


def escolher_tipo_mensagem():
  print("Escolha o tipo de mensagem:")
  print("1. Mensagem de saudação")
  print("2. Mensagem de despedida")
  print("3. Mensagem de agradecimento")
  print("4. Mensagem personalizada")

  escolha = input("Digite o número da sua escolha: ")

  if escolha == "1":
    return "Olá! Tenha um ótimo dia!"
  elif escolha == "2":
    return "Até logo! Foi ótimo conversar com você."
  elif escolha == "3":
    return "Obrigado pela sua ajuda!"
  elif escolha == "4":
    return criar_mensagem_personalizada()
  else:
    return "Escolha inválida."


def main():
  mensagem = escolher_tipo_mensagem()
  print("\nMensagem:")
  print(mensagem)


if __name__ == "__main__":
  main()