produto = float(input("Digite o valor do produto: "))
quantidade = float(input("Digite a quantidade de produtos: "))

if quantidade < 10:
    desconto = 0
elif quantidade < 20:
    desconto = 0.1
else:
    desconto = 0.2

sd = quantidade * produto
cd = produto * (1 - desconto)
vt = quantidade * cd
vd = quantidade * produto * desconto
pd = desconto * 100

print(f"Valor total sem desconto: {sd:.2f}")
print(f"Valor unitiário: R$ {produto:.2f}")
print(f"Valor com desconto: R${vt:.2f} ({pd:.0f}% de desconto)")
print(f"Valor total: R${vt:.2f} (desconto total: R$ {vd:.2f})")

