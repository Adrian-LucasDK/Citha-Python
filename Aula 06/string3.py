def pali(palavra):
    return palavra == palavra[::-1]

palavra = input("Digite uma palavra: ")
if pali(palavra):
    print(f"'{palavra}' é um palíndromo.")
else:
    print(f"'{palavra}' não é um palíndromo.")