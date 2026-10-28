import math

def calcular_hipotenusa(cateto_a, cateto_b):
    hipotenusa = math.hypot(cateto_a, cateto_b)
    return hipotenusa

cateto_a = float(input("Digite o primeiro cateto: "))
cateto_b = float(input("Digite o segundo cateto: "))

hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)

print(f"Hipotenusa: {hipotenusa:.2f}")