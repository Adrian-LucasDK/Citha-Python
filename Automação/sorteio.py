import random

def sorteio():
    alunos = [
        "jose", "ana", "pedro"
        "julia", "maria", "fabiana"
    ]
    escolhe = random.choice(alunos)
    print(f"o aluno escolhido foi: {escolhe}")

sorteio()