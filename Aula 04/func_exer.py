#Iniciando a função com o nome de area, e passando dois parâmetros, base e altura. Dentro da função, calculamos a área do triângulo e imprimimos o resultado na tela. 
def area(base, altura):
    area = base * altura / 2
    print("A área do triângulo é:", area)

#Iniciando as váriaveis base e altura
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))
#Chamando a função area e passando os parâmetros base e altura
area(base, altura)