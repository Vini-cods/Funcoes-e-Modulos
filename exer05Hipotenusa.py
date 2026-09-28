import math

def calcular_hipotenusa(cateto_a, cateto_b):
    hipotenusa = math.sqrt((cateto_a ** 2) + (cateto_b ** 2))
    return hipotenusa

cateto_a = float(input("Digite o primeiro cateto: "))
cateto_b = float(input("Digite o segundo cateto: "))

hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)

print(f"Hipotenusa: {hipotenusa:.2f}")