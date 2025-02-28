km = float(input("Digite a distância que irá percorrer (em km): "))
consumo = float(input("Digite o consumo médio do veículo (km/l): "))
valor = float(input("Digite o valor do litro de combustível: "))

if consumo <= 0 or valor < 0 or km < 0:
    print("Erro: Certifique-se de que os valores são positivos e o consumo não é zero.")
else:
    custo = (km / consumo) * valor
    print(f"O custo da viagem será de: R$ {custo:.2f}")
