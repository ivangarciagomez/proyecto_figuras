from lib import cuadrado
print("Proyecto Figuras")
lado = 4
print(f"El area de un cuadrado de lado {lado} es: {cuadrado.get_area(lado)}")

import math

def get_area(radio: float) -> float:
    """Calcula el área de un círculo dado su radio."""
    return math.pi * (radio ** 2)