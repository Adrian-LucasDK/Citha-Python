def funcao(po):
    if po.lower() == "sim":
        print("Tem café")
    elif po.lover() == "não":
        print("Não tem café")
    else:
        print("Comando inválido, digite sim ou não")

po = input("Você tem pó de café? ")

(funcao(po))