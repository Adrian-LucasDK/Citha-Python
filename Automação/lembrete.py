import time

def lembrete(intervalo=10):
    contador = 1
    while True:
        print(f"\n Tempo encerrado(Lembrete{contador})")
        contador += 1
        time.sleep(intervalo*60)

lembrete()