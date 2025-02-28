#Iniciando as varáveis 
qp = 0
qi = 0

#Repetição para receber 5 números
for i in range(5):
    num = int (input("Digite um numero: \n"))

#Condição para verificar se o número é par ou impar
    if num % 2 == 0:
        qp = qp + 1

    else:
        qi = qi + 1

#Imprimindo os resultados
print("Os números pares são: ", qp)
print("Os números impares são: ", qi)

