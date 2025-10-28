from typing import Any, List
from pprint import pformat, pprint
from dataclasses import dataclass
from collections import deque
from queue import PriorityQueue
from disjunto import Conjunto_disjunto

@dataclass(unsafe_hash=True, order=True)
class Punto:
    x: int
    y: int
    red: int
    green: int
    blue: int

@dataclass(unsafe_hash=True, order=True)
class Punto_Grafo:
    x: int
    y: int

@dataclass(unsafe_hash=True, order=True)
class Vertice:
    dato: Punto_Grafo

@dataclass(unsafe_hash=True, order=True)
class AristaNoDirigida:
    origen: Vertice
    destino: Vertice
    ponderacion: Any

@dataclass(unsafe_hash=True, order=True)
class Adyacente:
    destino: Vertice
    ponderacion: Any

class Grafo_No_Dirigido:
    def __init__(self):
        self.aristas: List[AristaNoDirigida] = []
        self.lista_adyacentes = {}
        self.recorrido = []

    def agregar_arista(self, arista: AristaNoDirigida):
        if arista in self.aristas:
            return
        self.aristas.append(arista)

    def crear_diccionario(self):
        for arista in self.aristas:
            origen = arista.origen
            destino = arista.destino
            ponderacion = arista.ponderacion

            if origen not in self.lista_adyacentes:
                self.lista_adyacentes[origen] = [Adyacente(destino=destino, ponderacion=ponderacion)]
            else:
                self.lista_adyacentes[origen].append(Adyacente(destino=destino, ponderacion=ponderacion))

            if destino not in self.lista_adyacentes:
                self.lista_adyacentes[destino] = [Adyacente(destino=origen, ponderacion=ponderacion)]
            else:
                self.lista_adyacentes[destino].append(Adyacente(destino=origen, ponderacion=ponderacion))

    def lista_de_adyacencia_to_string(self):
        self.crear_diccionario()
        return pformat(self.lista_adyacentes)

    def algoritmo_kruskal(self):
        grafo_resultante = Grafo_No_Dirigido()
        lista_ordenada = sorted(self.aristas, key=lambda arista: arista.ponderacion, reverse=True)
        cd = Conjunto_disjunto()
        self.crear_diccionario()
        cd.make_set(self.lista_adyacentes.keys())
        pprint(cd.conjunto)

        while len(lista_ordenada) > 0:
            arista = lista_ordenada[0]
            del lista_ordenada[0]
            if cd.find_set(arista.origen) != cd.find_set(arista.destino):
                grafo_resultante.agregar_arista(arista)
                cd.union_set(arista.origen, arista.destino)
                pprint(cd.conjunto)
        return grafo_resultante
