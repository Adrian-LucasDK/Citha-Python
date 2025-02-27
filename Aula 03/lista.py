
#Autor: Adrian Lucas Souza da Silva

# Criando uma lista em Python
lista = ["Arroz", "Feijão", "Açúcar", "Farinha", "Oléo"]

# Imprimindo a lista a inicial
print("Lista inicial:", lista)

# Acessando um item da lista
print("Item 1: ", lista[0])

# Acessando outro item da lista
print("Item 2: ", lista[1])

# Alterando um item da lista
lista[0] = "Leite"

# Imprimido a Lista modificada
print("Lista Modificada: ", lista)

# Deletando um item da lista
del lista[4]

# Imprimido a Lista Final
print("Lista Final: ", lista)

# Adicionando um item a lista
lista.append("Sal")

# Imprimido a lista ápos a adição de um item
print("Lista após a adição de um item: ", lista)

#Organizando a lista
lista.sort()

# Imprimindo a lista organizada
print("Lista organizada: ", lista)

#Nova lista númerica
lista1 = [73, 39, 100, 23, 45, 67]

#Organiznadno a lista de forma decrescente
lista1.sort(reverse=True)

#Imprimindo a lista organizada de forma decrescente
print("Lista Organizada em Ordem Decrescte",lista1)

#Adicionando um item a lista
lista1.append(10)

#Ordenando a lista de forma crescente
lista1.sort()

#Imprimindo a lista organizada de forma crescente
print("Lista Organizada em Ordem Crescente",lista1)

#Maior e menor valor da lista
maior = max(lista1)
menor = min(lista1)

#Imprimindo o maior e o menor valor da lista
print("Maior valor: ", maior)
print("Menor valor: ", menor)

#Adicionando mais de um item a lista
lista1.append(94)
lista1.append(12)
lista1.append(56)
lista1.append(78)
lista1.append(23)
lista1.append(45)

#Imprimindo a lista com mais de um item adicionado
print(lista1)

#Acessando um item da lista com mais de um item adicionado
print("elemento da posição 3: ", lista1[3])