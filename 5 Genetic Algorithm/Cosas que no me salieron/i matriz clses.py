a = [0, 6, 0, 0, 0, 0]
b = [6, 0, 2, 0, 0, 0]
c = [0, 2, 0, 3, 3, 3]
d = [0, 0, 3, 0, 0, 0]
e = [0, 0, 3, 0, 0, 0]


class Ruta:
    def __init__(self, puntoa: str, puntob: str, time: int, linea: str):
        self.puntoa = puntoa
        self.puntob = puntob
        self.time = time
        self.linea = linea

    def __str__(self):
        return f'Ruta: {self.puntoa} <-> {self.puntob} (Linea {self.linea})'


rutas = [Ruta('a', 'b', 6, '1'),
         Ruta('b', 'c', 2, '1'),
         Ruta('c', 'd', 3, '2'),
         Ruta('c', 'e', 3, '3'),]
