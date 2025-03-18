import time
import random

lista = []

while True:
    lista.append(input("Digite os nomes: "))
    maisnome = input("deseja continuar: ").lower()
    if maisnome == "n":
        break

def msg(lista1):
    print(f"Boa noite {random.choice(lista1)}")
    time.sleep(2)
    print("Python")

msg(lista)