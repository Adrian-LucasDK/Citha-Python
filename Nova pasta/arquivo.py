with open ("texto.txt", "w", encoding="utf-8") as file:
    for i in range(3):
        frase = input(f"Digite a frase {i+1}ª frase: ")
        file.write(frase + "\n")
print("Frases salvas com sucesso!")

