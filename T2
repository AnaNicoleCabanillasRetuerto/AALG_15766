import random
import math

def distancia_origen(coord):
    x, y = coord
    return math.sqrt(x**2 + y**2)

def coordenada_mas_alejada(coords):
    if not coords:
        return None
    if len(coords) == 1:
        x, y = coords[0]
        return coords[0] if x > 0 and y < 0 else None

    mitad = len(coords) // 2
    izquierda = coordenada_mas_alejada(coords[:mitad])
    derecha = coordenada_mas_alejada(coords[mitad:])

    if izquierda is None:
        return derecha
    if derecha is None:
        return izquierda

    return izquierda if distancia_origen(izquierda) > distancia_origen(derecha) else derecha

n = int(input("¿Cuántos pares de coordenadas deseas generar?: "))

matriz = [[random.randint(-81, 81), random.randint(-81, 81)] for _ in range(n)]

print("\nCoordenadas generadas:")
for par in matriz:
    print(par)

resultado = coordenada_mas_alejada(matriz)

if resultado:
    print(f"\nLa coordenada más alejada del origen con X > 0 e Y < 0 es: {resultado}")
    print(f"Distancia: {distancia_origen(resultado):.2f}")
else:
    print("\nNo se encontró ninguna coordenada con X > 0 e Y < 0.")