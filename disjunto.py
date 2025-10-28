class Conjunto_disjunto:
    def __init__(self):
        self.conjunto = []

    def make_set(self, vertices: list):
        for vertice in vertices:
            conjunto = [vertice]
            self.conjunto.append(conjunto)

    def find_set(self, vertice):
        i = 0
        while i < len(self.conjunto):
            if vertice in self.conjunto[i]:
                return i
            i += 1

    def union_set(self, origen, destino):
        posicion_origen = self.find_set(origen)
        posicion_destino = self.find_set(destino)
        self.conjunto[posicion_origen] += self.conjunto[posicion_destino]
        del self.conjunto[posicion_destino]
