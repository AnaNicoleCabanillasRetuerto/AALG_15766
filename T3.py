laberinto_letrita = [
    ['F','1','1','3','0','1','1','1','4'],
    ['3','0','0','1','0','1','0','0','1'],
    ['1','1','0','1','1','1','1','0','1'],
    ['0','1','0','1','0','0','1','0','1'],
    ['1','1','1','1','1','1','3','1','1'],
    ['3','0','1','0','0','0','1','0','1'],
    ['1','1','1','1','3','1','1','1','1'],
    ['1','0','0','1','0','1','0','0','4'],
    ['I','1','3','1','0','1','1','1','1']
]

lab = []
for fila in laberinto_letrita:
    nueva_fila = []
    for celda in fila:
        if celda == '0':
            nueva_fila.append(0)
        elif celda in ['F', 'I']:
            nueva_fila.append(1)
        else:
            nueva_fila.append(int(celda))
    lab.append(nueva_fila)

filas, cols = 9, 9
inicio = (8, 0)
fin = (0, 0)
visitado = [[False]*cols for _ in range(filas)]
camino = []
puntaje_total = [0]

def buscar(i, j, puntos, path):
    if i < 0 or i >= filas or j < 0 or j >= cols:
        return False
    if lab[i][j] == 0 or visitado[i][j]:
        return False

    puntos += lab[i][j]
    path.append((i, j))
    visitado[i][j] = True

    if (i, j) == fin:
        if puntos == 23:
            puntaje_total[0] = puntos
            return True
        else:
            path.pop()
            visitado[i][j] = False
            return False

    if (buscar(i - 1, j, puntos, path) or
        buscar(i, j + 1, puntos, path) or
        buscar(i + 1, j, puntos, path) or
        buscar(i, j - 1, puntos, path)):
        return True

    path.pop()
    visitado[i][j] = False
    return False

print("Laberinto original:")
for fila in laberinto_letrita:
    print(' '.join(fila))

if buscar(inicio[0], inicio[1], 0, camino):
    print(f"\n Camino encontrado. Su puntaje total es: {puntaje_total[0]} puntos.")
    print("Camino (coordenadas):", camino)

    resultado = [fila[:] for fila in laberinto_letrita]
    for i, j in camino:
        if resultado[i][j] not in ['I', 'F']:
            resultado[i][j] = '*'

    print("\nLaberinto con camino marcado:")
    for fila in resultado:
        print(' '.join(fila))
else:
    print("\nNo se encontró un camino que sume exactamente 23 puntos.")