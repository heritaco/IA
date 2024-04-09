
class Ruta:
    """Clase para representar una ruta entre dos puntos de la ciudad"""

    def __init__(self, a: str, b: str, time: int, linea: str):
        self.start = a
        self.end = b
        self.time = time
        self.linea = linea

    def __str__(self):
        return f'Ruta: de {self.start} a {self.end} (Linea {self.linea})'


estaciones = [
    "Atlalilco",          # 0
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


rutas = [
    # Ruta 1
    Ruta(estaciones[31], estaciones[1], 6, '1'),     # Tacubaya a Balderas
    # Balderas a Salto del Agua
    Ruta(estaciones[1], estaciones[28], 1, '1'),
    # Salto del Agua a Pino Suárez
    Ruta(estaciones[28], estaciones[26], 2, '1'),
    Ruta(estaciones[26], estaciones[4], 2, '1'),     # Pino Suárez a Candelaria
    Ruta(estaciones[4], estaciones[29], 1, '1'),     # Candelaria a San Lázaro
    # San Lázaro a Gómez Farías
    Ruta(estaciones[29], estaciones[14], 4, '1'),
    Ruta(estaciones[14], estaciones[25], 2, '1'),    # Gómez Farías a Pantitlán

    # Ruta 2
    # Cuatro Caminos a Tacubaya
    Ruta(estaciones[9], estaciones[31], 1, '2'),
    Ruta(estaciones[31], estaciones[16], 7, '2'),    # Tacubaya a Hidalgo
    Ruta(estaciones[16], estaciones[3], 1, '2'),     # Hidalgo a Bellas Artes
    # Bellas Artes a Pino Suárez
    Ruta(estaciones[3], estaciones[26], 3, '2'),
    Ruta(estaciones[26], estaciones[6], 2, '2'),     # Pino Suárez a Chabacano
    Ruta(estaciones[6], estaciones[12], 6, '2'),     # Chabacano a Ermita
    Ruta(estaciones[12], estaciones[32], 1, '2'),    # Ermita a Tasqueña

    # Ruta 3
    # Indios Verdes a Deportivo 18 de Marzo
    Ruta(estaciones[17], estaciones[10], 1, '3'),
    # Deportivo 18 de Marzo a La Raza
    Ruta(estaciones[10], estaciones[20], 2, '3'),
    Ruta(estaciones[20], estaciones[15], 2, '3'),   # La Raza a Guerrero
    Ruta(estaciones[15], estaciones[16], 1, '3'),   # Guerrero a Hidalgo
    Ruta(estaciones[16], estaciones[1], 2, '3'),    # Hidalgo a Balderas
    Ruta(estaciones[1], estaciones[5], 3, '3'),     # Balderas a Centro Médico
    Ruta(estaciones[5], estaciones[35], 4, '3'),    # Centro Médico a Zapata
    Ruta(estaciones[35], estaciones[34], 2, '3'),    # Zapata a Universidad

    # Ruta 4
    # Martín Carrera a Consulado
    Ruta(estaciones[21], estaciones[8], 3, '4'),
    Ruta(estaciones[8], estaciones[23], 2, '4'),    # Consulado a Morelos
    Ruta(estaciones[23], estaciones[4], 1, '4'),    # Morelos a Candelaria
    Ruta(estaciones[4], estaciones[19], 2, '4'),    # Candelaria a Jamaica

    # Ruta 5
    # Politécnico a Instituto del Petróleo
    Ruta(estaciones[27], estaciones[18], 1, '5'),
    # Instituto del Petróleo a La Raza
    Ruta(estaciones[18], estaciones[20], 2, '5'),
    Ruta(estaciones[20], estaciones[8], 3, '5'),   # La Raza a Consulado
    Ruta(estaciones[8], estaciones[24], 3, '5'),   # Consulado a Oceanía
    Ruta(estaciones[24], estaciones[25], 3, '5'),  # Oceanía a Pantitlán

    # Ruta 6
    # El Rosario a Instituto del Petróleo
    Ruta(estaciones[11], estaciones[18], 6, '6'),
    # Instituto del Petróleo a Deportivo 18 de Marzo
    Ruta(estaciones[18], estaciones[10], 2, '6'),
    # Deportivo 18 de Marzo a Martín Carrera
    Ruta(estaciones[10], estaciones[21], 2, '6'),

    # Ruta 7
    Ruta(estaciones[11], estaciones[30], 4, '7'),  # El Rosario a Tacuba
    Ruta(estaciones[30], estaciones[31], 5, '7'),  # Tacuba a Tacubaya
    Ruta(estaciones[31], estaciones[22], 3, '7'),  # Tacubaya a Mixcoac
    # Mixcoac a Barranca del Muerto
    Ruta(estaciones[22], estaciones[2], 1, '7'),

    # Ruta 8
    Ruta(estaciones[13], estaciones[3], 1, '8'),   # Garibaldi a Bellas Artes
    # Bellas Artes a Salto del Agua
    Ruta(estaciones[3], estaciones[28], 2, '8'),
    Ruta(estaciones[28], estaciones[6], 3, '8'),   # Salto del Agua a Chabacano
    Ruta(estaciones[6], estaciones[0], 8, '8'),    # Chabacano a Atlalilco

    # Ruta 9
    Ruta(estaciones[31], estaciones[5], 3, '9'),   # Tacubaya a Centro Médico
    Ruta(estaciones[5], estaciones[6], 2, '9'),    # Centro Médico a Chabacano
    Ruta(estaciones[6], estaciones[19], 1, '9'),   # Chabacano a Jamaica
    Ruta(estaciones[19], estaciones[25], 5, '9'),  # Jamaica a Pantitlán

    # Ruta 12
    Ruta(estaciones[22], estaciones[35], 3, '12'),  # Mixcoac a Zapata
    Ruta(estaciones[35], estaciones[12], 3, '12'),  # Zapata a Ermita
    Ruta(estaciones[12], estaciones[0], 2, '12'),  # Ermita a Atlalilco
    Ruta(estaciones[0], estaciones[33], 1, '12'),   # Atlalilco a Tláhuac

    # Ruta B
    Ruta(estaciones[15], estaciones[13], 1, 'B'),   # Guerrero a Garibaldi
    Ruta(estaciones[13], estaciones[23], 3, 'B'),   # Garibaldi a Morelos
    Ruta(estaciones[23], estaciones[29], 1, 'B'),   # Morelos a San Lázaro
    Ruta(estaciones[29], estaciones[24], 3, 'B'),   # San Lázaro a Oceanía
    Ruta(estaciones[24], estaciones[7], 1, 'B'),     # Oceanía a Ciudad Azteca

    # Ruta 1
    Ruta(estaciones[1], estaciones[31], 6, '1'),     # Balderas a Tacubaya
    # Salto del Agua a Balderas
    Ruta(estaciones[28], estaciones[1], 1, '1'),
    # Pino Suárez a Salto del Agua
    Ruta(estaciones[26], estaciones[28], 2, '1'),
    Ruta(estaciones[4], estaciones[26], 2, '1'),     # Candelaria a Pino Suárez
    Ruta(estaciones[29], estaciones[4], 1, '1'),     # San Lázaro a Candelaria
    # Gómez Farías a San Lázaro
    Ruta(estaciones[14], estaciones[29], 4, '1'),
    Ruta(estaciones[25], estaciones[14], 2, '1'),    # Pantitlán a Gómez Farías

    # Ruta 2
    # Tacubaya a Cuatro Caminos
    Ruta(estaciones[31], estaciones[9], 1, '2'),
    Ruta(estaciones[16], estaciones[31], 7, '2'),    # Hidalgo a Tacubaya
    Ruta(estaciones[3], estaciones[16], 1, '2'),     # Bellas Artes a Hidalgo
    # Pino Suárez a Bellas Artes
    Ruta(estaciones[26], estaciones[3], 3, '2'),
    Ruta(estaciones[6], estaciones[26], 2, '2'),     # Chabacano a Pino Suárez
    Ruta(estaciones[12], estaciones[6], 6, '2'),     # Ermita a Chabacano
    Ruta(estaciones[32], estaciones[12], 1, '2'),    # Tasqueña a Ermita

    # Ruta 3
    # Deportivo 18 de Marzo a Indios Verdes
    Ruta(estaciones[10], estaciones[17], 1, '3'),
    # La Raza a Deportivo 18 de Marzo
    Ruta(estaciones[20], estaciones[10], 2, '3'),
    Ruta(estaciones[15], estaciones[20], 2, '3'),   # Guerrero a La Raza
    Ruta(estaciones[16], estaciones[15], 1, '3'),   # Hidalgo a Guerrero
    Ruta(estaciones[1], estaciones[16], 2, '3'),    # Balderas a Hidalgo
    Ruta(estaciones[5], estaciones[1], 3, '3'),     # Centro Médico a Balderas
    Ruta(estaciones[35], estaciones[5], 4, '3'),    # Zapata a Centro Médico
    Ruta(estaciones[34], estaciones[35], 2, '3'),    # Universidad a Zapata

    # Ruta 4
    # Consulado a Martín Carrera
    Ruta(estaciones[8], estaciones[21], 3, '4'),
    Ruta(estaciones[23], estaciones[8], 2, '4'),    # Morelos a Consulado
    Ruta(estaciones[4], estaciones[23], 1, '4'),    # Candelaria a Morelos
    Ruta(estaciones[19], estaciones[4], 2, '4'),    # Jamaica a Candelaria

    # Ruta 5
    # Instituto del Petróleo a Politécnico
    Ruta(estaciones[18], estaciones[27], 1, '5'),
    # La Raza a Instituto del Petróleo
    Ruta(estaciones[20], estaciones[18], 2, '5'),
    Ruta(estaciones[8], estaciones[20], 3, '5'),   # Consulado a La Raza
    Ruta(estaciones[24], estaciones[8], 3, '5'),   # Oceanía a Consulado
    Ruta(estaciones[25], estaciones[24], 3, '5'),  # Pantitlán a Oceanía

    # Ruta 6
    # Instituto del Petróleo a El Rosario
    Ruta(estaciones[18], estaciones[11], 6, '6'),
    # Deportivo 18 de Marzo a Instituto del Petróleo
    Ruta(estaciones[10], estaciones[18], 2, '6'),
    # Martín Carrera a Deportivo 18 de Marzo
    Ruta(estaciones[21], estaciones[10], 2, '6'),

    # Ruta 7
    Ruta(estaciones[30], estaciones[11], 4, '7'),  # Tacuba a El Rosario
    Ruta(estaciones[31], estaciones[30], 5, '7'),  # Tacubaya a Tacuba
    Ruta(estaciones[22], estaciones[31], 3, '7'),  # Mixcoac a Tacubaya
    # Barranca del Muerto a Mixcoac
    Ruta(estaciones[2], estaciones[22], 1, '7'),

    # Ruta 8
    Ruta(estaciones[3], estaciones[13], 1, '8'),   # Bellas Artes a Garibaldi
    # Salto del Agua a Bellas Artes
    Ruta(estaciones[28], estaciones[3], 2, '8'),
    Ruta(estaciones[6], estaciones[28], 3, '8'),   # Chabacano a Salto del Agua
    Ruta(estaciones[0], estaciones[6], 8, '8'),    # Atlalilco a Chabacano

    # Ruta 9
    Ruta(estaciones[5], estaciones[31], 3, '9'),   # Centro Médico a Tacubaya
    Ruta(estaciones[6], estaciones[5], 2, '9'),    # Chabacano a Centro Médico
    Ruta(estaciones[19], estaciones[6], 1, '9'),   # Jamaica a Chabacano
    Ruta(estaciones[25], estaciones[19], 5, '9'),  # Pantitlán a Jamaica

    # Ruta 12
    Ruta(estaciones[35], estaciones[22], 3, '12'),  # Zapata a Mixcoac
    Ruta(estaciones[12], estaciones[35], 3, '12'),  # Ermita a Zapata
    Ruta(estaciones[0], estaciones[12], 2, '12'),  # Atlalilco a Ermita
    Ruta(estaciones[33], estaciones[0], 1, '12'),   # Tláhuac a Atlalilco

    # Ruta B
    Ruta(estaciones[13], estaciones[15], 1, 'B'),   # Garibaldi a Guerrero
    Ruta(estaciones[23], estaciones[13], 3, 'B'),   # Morelos a Garibaldi
    Ruta(estaciones[29], estaciones[23], 1, 'B'),   # San Lázaro a Morelos
    Ruta(estaciones[24], estaciones[29], 3, 'B'),   # Oceanía a San Lázaro
    Ruta(estaciones[7], estaciones[24], 1, 'B')     # Ciudad Azteca a Oceanía


]
