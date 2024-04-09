"""FC3 Genetic Alorithm"""

from typing import List, Tuple


class Ruta:
    """Clase para representar una ruta entre dos puntos de la ciudad"""

    def __init__(self, puntoa: str, puntob: str, time: int, linea: str):
        self.puntoa = puntoa
        self.puntob = puntob
        self.time = time
        self.linea = linea

    def __str__(self):
        return f'Ruta: {self.puntoa} <-> {self.puntob} (Linea {self.linea})'


estaciones = ["Atlalilco",          # 0
              "Balderas",           # 1
              "Barranca del Muerto",  # 2
              "Bellas Artes",       # 3
              "Candelaria",         # 4
              "Centro Médico",      # 5
              "Chabacano",          # 6
              "Ciudad Azteca",      # 7
              "Consulado",          # 8
              "Cuatro Caminos",     # 9
              "Deportivo 18 de Marzo",  # 10
              "El Rosario",         # 11
              "Ermita",             # 12
              "Garibaldi",          # 13
              "Gómez Farías",       # 14
              "Guerrero",           # 15
              "Hidalgo",            # 16
              "Indios Verdes",      # 17
              "Instituto del Petroleo",  # 18
              "Jamaica",            # 19
              "La Raza",            # 20
              "Martín Carrera",     # 21
              "Mixcoac",            # 22
              "Morelos",            # 23
              "Oceanía",            # 24
              "Pantitlán",          # 25
              "Pino Suárez",        # 26
              "Politécnico",        # 27
              "Salto del Agua",     # 28
              "San Lázaro",         # 29
              "Tacuba",             # 30
              "Tacubaya",           # 31
              "Tasqueña",           # 32
              "Tláhuac",            # 33
              "Universidad",        # 34
              "Zapata"              # 35
              ]


rutas = [Ruta(estaciones[11], estaciones[18], 6, '6'),
         Ruta(estaciones[11], estaciones[8], 6, '6'),
         Ruta(estaciones[18], estaciones[20], 2, '5'),
         Ruta(estaciones[20], estaciones[8], 3, '5'),
         Ruta(estaciones[20], estaciones[10], 3, '5')]


def calculate_distance(start: str, end: str, rutas: List[Ruta]) -> Tuple[str, int]:
    """Calcula la distancia entre dos puntos de la ciudad y la ruta a seguir para llegar de uno a otro"""
    total_time = 0
    current_station = start
    path = []
    while current_station != end:
        for ruta in rutas:
            if ruta.puntoa == current_station:
                total_time += ruta.time
                current_station = ruta.puntob
                path.append((ruta.linea, ruta.puntoa, ruta.puntob))
                break

    path_str = f"De {start} a {end} tarde {total_time}\nEl camino es\n "
    for paths in path:
        path_str += f"De {paths[1]} a {paths[2]} con la linea {paths[0]}\n "
    return path_str, total_time


# Usage
path_str, total_time = calculate_distance('El Rosario', 'Consulado', rutas)
print(path_str)
print(total_time)
