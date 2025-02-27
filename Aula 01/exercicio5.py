#Input: Duas notas
n1 = float (input("Digite sua primeira nota: "))
n2 = float (input("Digite sua segunda nota: "))

# Cálculo da média
media = (n1+n2) / 2

# Condição para saber se o aluno foi aprovado
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")