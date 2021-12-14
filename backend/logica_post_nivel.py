from PyQt5.QtCore import QObject, pyqtSignal
import parametros as p
import os

class LogicaPostNivel(QObject):

    def __init__(self):
        super().__init__()

    def guardar_jugadores(self, usuario, puntaje_total):
        self.mensaje_ganador = f"{usuario}, {puntaje_total}"
        with open("puntajes.txt", "a", encoding = "utf-8") as archivo_puntajes:
            archivo_puntajes.write(f"{self.mensaje_ganador}\n")