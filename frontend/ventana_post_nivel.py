from PyQt5.QtCore  import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import parametros as p 

nombre_ventana, clase_base = uic.loadUiType(p.RUTA_UI_VENTANA_POST_NIVEL)
class VentanaPostNivel(nombre_ventana, clase_base):
    senal_siguiente_nivel_ronda = pyqtSignal()
    senal_siguiente_nivel_threadr = pyqtSignal()
    senal_siguiente_nivel_threadl = pyqtSignal()
    senal_siguiente_nivel_ventana = pyqtSignal(str)
    senal_reordenar_labels = pyqtSignal()
    senal_guardar_puntajes = pyqtSignal(str, int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Ventana post nivel")
        self.setWindowIcon(QIcon(p.RUTA_ICONO))
        self.exit_button.clicked.connect(self.salir)

    def mostrar_ventana_victoria(self, nivel, puntaje_total,
    puntaje_nivel, vidas_restantes, monedas_totales, usuario):
        self.usuario = usuario
        self.puntaje_total = puntaje_total
        self.label_seguir_juego.setStyleSheet("background-color:#4bf057;\
    border-radius: 5px; border: 1px solid black")
        self.label_seguir_juego.setText("Puedes \
seguir con el siguiente nivel")
        self.next_level_button.clicked.connect(self.pasar_nivel)
        self.label_nivel.setText(str(nivel))
        self.label_puntaje_total.setText(str(puntaje_total))
        self.label_puntaje_nivel.setText(str(puntaje_nivel))
        self.label_vidas_restantes.setText(str(vidas_restantes))
        self.label_monedas_total.setText(str(monedas_totales))
        self.show()

    def mostrar_ventana_derrota(self, nivel, puntaje_total, 
    puntaje_nivel, vidas_restantes, monedas_totales):
        self.puntaje_total = puntaje_total
        self.label_seguir_juego.setStyleSheet("background-color:#f04b4b ;\
         border-radius: 5px; border: 1px solid black ")
        self.label_seguir_juego.setText("No puedes seguir jugando :(")
        self.next_level_button.setEnabled(False)
        self.label_nivel.setText(str(nivel))
        self.label_puntaje_total.setText(str(puntaje_total))
        self.label_puntaje_nivel.setText(str(puntaje_nivel))
        self.label_vidas_restantes.setText(str(vidas_restantes))
        self.label_monedas_total.setText(str(monedas_totales))
        self.show()

    def salir(self):
        self.close()
        self.senal_guardar_puntajes.emit(self.usuario, self.puntaje_total)

    def pasar_nivel(self):
        self.senal_siguiente_nivel_ronda.emit()
        self.senal_siguiente_nivel_threadl.emit()
        self.senal_siguiente_nivel_threadr.emit()
        self.senal_reordenar_labels.emit()
        self.senal_siguiente_nivel_ventana.emit(self.usuario)
        self.close()