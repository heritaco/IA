from typing import List, Tuple


class Ruta:
    def __init__(self, puntoa: str, puntob: str, time: int, linea: str):
        self.puntoa = puntoa
        self.puntob = puntob
        self.time = time
        self.linea = linea

    def __str__(self):
        return f'Ruta: {self.puntoa} <-> {self.puntob} (Linea {self.linea})'


estaciones = ['El Rosario', 'Instituto', 'La Raza',
              'Consulado', 'Deportivo 18 de Marzo']

rutas = [Ruta(estaciones[0], estaciones[1], 6, '6'),
         Ruta(estaciones[1], estaciones[2], 2, '5'),
         Ruta(estaciones[2], estaciones[3], 3, '5'),
         Ruta(estaciones[2], estaciones[4], 3, '5')]

for cada_ruta in rutas:
    print('De', cada_ruta.puntoa, 'a', cada_ruta.puntob,
          'en la linea', cada_ruta.linea, 'tarda', cada_ruta.time)


def calculate_distance(start: str, end: str, rutas: List[Ruta]) -> Tuple[int, List[str]]:
    total_time = 0
    current_station = start
    lineas = []
    while current_station != end:
        for ruta in rutas:
            if ruta.puntoa == current_station:
                total_time += ruta.time
                current_station = ruta.puntob
                lineas.append(ruta.linea)
                break
    return total_time, lineas


# Usage
time, lineas = calculate_distance('El Rosario', 'Consulado', rutas)
print('del rosario a consulado tarde', time,
      'y las lineas que tomo son', lineas)
