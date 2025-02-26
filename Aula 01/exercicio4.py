peso = float(input("Digite seu peso: "))
idade = float(input("Digite sua idade: "))

if peso > 50 and idade >= 16 and idade <= 69:
    print("Você pode doar sangue")
else:
    print("Você não pode doar sangue")