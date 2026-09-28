import math

def calcular_area_circulo(raio):
    return math.pi * (raio ** 2)

raio = float(input("Digite o raio do circulo: "))
area = calcular_area_circulo(raio)

print(f"Area do circulo: {area:.2f}")