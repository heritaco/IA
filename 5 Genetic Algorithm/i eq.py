class Ruta:
    # The constructor for the Ruta class. It initializes the instance variables.
    def __init__(self, puntoa, puntob, distancia, linea):
        self.puntoa = puntoa  # The starting point of the route
        self.puntob = puntob  # The ending point of the route
        self.distancia = distancia  # The distance of the route
        self.linea = linea  # The line of the route

    # This method returns a string representation of the Ruta object.
    def __str__(self):
        return f'Ruta: {self.puntoa} <-> {self.puntob} (Linea {self.linea})'

    # This method returns a string representation of the Ruta object. It calls the __str__ method.
    def __repr__(self):
        return str(self)

    # This method checks if two Ruta objects are equal. Two Ruta objects are considered equal if they have the same starting and ending points, regardless of the order.
    def __eq__(self, other):
        return (self.puntoa == other.puntoa and self.puntob == other.puntob) or \
               (self.puntoa == other.puntob and self.puntob == other.puntoa)

    # This method returns a hash value for a Ruta object. The hash value is computed based on the starting and ending points of the route, regardless of the order.
    def __hash__(self):
        return hash((min(self.puntoa, self.puntob), max(self.puntoa, self.puntob)))