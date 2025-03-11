while True:
    es = input("Digite se você esbarrou em alguém: ").strip().lower()

    if es == "não":
        print("Siga em frente")
        break
    elif es == "sim":
        print("Soryy")
    else:       
        print("Comando inválido, digite sim ou não")