from PyQt5.QtCore import QObject, pyqtSignal
import parametros as p
import os

class LogicaRanking(QObject):

    senal_enviar_jugadores = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def tomar_segundo(self, jugador):
        return int(jugador[1])

    def enviar_jugadores(self):
        lista_jugadores = []
        ranking_jugadores = []
        ruta_jugadores = os.path.join("puntajes.txt")
        with open(ruta_jugadores, "rt", encoding = "utf-8") as archivo_jugadores:
            for linea in archivo_jugadores:
                linea = linea.strip('\n').split(sep = ',', maxsplit = 2)
                lista_jugadores.append(linea)

## Idea sacada de https://www.programiz.com/python-programming/methods/list/sort
        lista_jugadores.sort(key = self.tomar_segundo, reverse = True)
        
        if len(lista_jugadores) > 0:
            for i in range(0, len(lista_jugadores)):
                jugador = f"{i+1}. {lista_jugadores[i][0]}      {lista_jugadores[i][1]} ptos"
                ranking_jugadores.append(jugador)
        
            
            self.senal_enviar_jugadores.emit(ranking_jugadores)

        else:
            pass

            