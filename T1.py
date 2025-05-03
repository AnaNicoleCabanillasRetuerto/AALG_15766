import random

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidosGanados = 0
        self.partidosPerdidos = 0
        self.setGanados = 0

# Crear variables globales
equipo1 = None
equipo2 = None

def RegistraSet(ganador):
    global equipo1, equipo2

    if ganador == 1:
        equipo1.setGanados += 1
    else:
        equipo2.setGanados += 1

    if equipo1.setGanados == 3:
        equipo1.partidosGanados += 1
        equipo2.partidosPerdidos += 1
        print(f"\n{equipo1.nombre} gana el partido con 3 sets contra {equipo2.setGanados}")
        equipo1.setGanados = 0
        equipo2.setGanados = 0
    elif equipo2.setGanados == 3:
        equipo2.partidosGanados += 1
        equipo1.partidosPerdidos += 1
        print(f"\n{equipo2.nombre} gana el partido con 3 sets contra {equipo1.setGanados}")
        equipo1.setGanados = 0
        equipo2.setGanados = 0

def Puntos():
    return random.randint(10, 28)

def PuntosExtras():
    return random.randint(0, 6)

def JugarPartido(equipo1, equipo2):
    while equipo1.setGanados < 3 and equipo2.setGanados < 3:
        puntos1 = Puntos()
        puntos2 = Puntos()

        while True:
            if puntos1 >= 25 or puntos2 >= 25:
                if abs(puntos1 - puntos2) >= 1 and max(puntos1, puntos2) >= 25:
                    if puntos1 > puntos2:
                        print(f"{equipo1.nombre} gana el set con {puntos1} puntos contra {puntos2}")
                        RegistraSet(1)
                    else:
                        print(f"{equipo2.nombre} gana el set con {puntos2} puntos contra {puntos1}")
                        RegistraSet(2)
                    break

            # Nadie gana todavía, se suman puntos extras
            puntos1 += PuntosExtras()
            puntos2 += PuntosExtras()
            print(f"Ningún equipo superó 25 puntos, sumando puntos extras: {equipo1.nombre} {puntos1}, {equipo2.nombre} {puntos2}")

def ResultadoTorneo():
    print("\nResultados del Torneo:")
    print(f"{equipo1.nombre}: Partidos Ganados: {equipo1.partidosGanados}, Partidos Perdidos: {equipo1.partidosPerdidos}")
    print(f"{equipo2.nombre}: Partidos Ganados: {equipo2.partidosGanados}, Partidos Perdidos: {equipo2.partidosPerdidos}")


def main():
    global equipo1, equipo2
    nombre1 = input("Nombre del Equipo 1: ")
    nombre2 = input("Nombre del Equipo 2: ")
    equipo1 = Equipo(nombre1)
    equipo2 = Equipo(nombre2)

    try:
        total_partidos = int(input("¿Cuántos partidos deben jugar ambos equipos? "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return

    for i in range(total_partidos):
        print(f"\n--- Jugando partido {i+1} ---")    
        JugarPartido(equipo1, equipo2)

    ResultadoTorneo()

if __name__ == "__main__":
    main()