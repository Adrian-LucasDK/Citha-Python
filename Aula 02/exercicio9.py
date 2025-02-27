#Input: Valor em R$ e valor da conversão em $
reais = float(input("Digite o valor em R$: "))
con = float(input("Digite o valor da conversão em $: "))

#Cálculo da conversão
dolar = reais / con

#Imprime o valor em dolar
print ("O valor de R$", reais, "em dolar é igual a $", dolar)