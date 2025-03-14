import matplotlib.pyplot as plt

paises = ["Brasil", "México"]
consumo = [21.6, 34.2]

plt.figure(figsize=(8,8))
plt.pie(consumo, labels=paises, autopct='%1.1f%%', colors=["blue", "red"],  startangle=90)

plt.title("Consumo de Ovos por mulhres (%)")

plt.show()