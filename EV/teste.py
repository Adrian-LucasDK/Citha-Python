def calcular_preco_com_desconto(produto, quantidade):
    if quantidade < 10:
        desconto = 0
    elif quantidade < 20:
        desconto = 0.1
    else:
        desconto = 0.2

    sd = quantidade * produto  # Valor total sem desconto
    cd = produto * (1 - desconto)  # Valor unitário com desconto
    vt = quantidade * cd  # Valor total com desconto
    vd = quantidade * produto * desconto  # Valor do desconto total
    pd = desconto * 100  # Porcentagem de desconto

    return sd, produto, vt, pd, vd


# Entrada de dados
produto = float(input("Digite o valor do produto: "))
quantidade = float(input("Digite a quantidade de produtos: "))

# Chamada da função
sd, produto, vt, pd, vd = calcular_preco_com_desconto(produto, quantidade)

# Exibição dos resultados
print(f"Valor total sem desconto: R$ {sd:.2f}")
print(f"Valor unitário: R$ {produto:.2f}")
print(f"Valor com desconto: R$ {vt:.2f} ({pd:.0f}% de desconto)")
print(f"Valor total com desconto: R$ {vt:.2f} (desconto total: R$ {vd:.2f})")
