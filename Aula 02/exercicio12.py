preço = float (input("Digite o preço do produto: "))
desc = float (input("Digite o desconto do produto: "))

pf = preço - (preço*desc/100)

print ("O preço final com desconto é igual: ", pf)