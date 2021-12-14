from PyQt5.QtCore  import pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QApplication
from parametros import MIN_CARACTERES, MAX_CARACTERES, RUTA_LOGO, RUTA_ICONO

## Obtencion datos archivo

class VentanaRanking(QWidget):

    senal_volver_inicio = pyqtSignal()
    senal_solicitar_jugadores = pyqtSignal()
    senal_recibir_jugadores = pyqtSignal(list)

    def __init__(self, tamano_ventana):
        super().__init__()
        self.init_gui(tamano_ventana)
        self.senal_solicitar_jugadores.emit()

    def init_gui(self, tamano_ventana):
        self.setWindowIcon(QIcon(RUTA_ICONO))
        ## """A continuacion se configurara la geometria de la ventana"""
        self.setWindowTitle("Ventana de Ranking")
        self.setGeometry(tamano_ventana)
        self.label_titulo = QLabel("RANKING DE PUNTAJES")
        self.label_1 = QLabel("1.", self)
        self.label_2 = QLabel("2.", self)
        self.label_3 = QLabel("3.", self)
        self.label_4 = QLabel("4.", self)
        self.label_5 = QLabel("5.", self)
        self.volver_button = QPushButton("Volver", self)
        self.volver_button.clicked.connect(self.volver)

        ## Estilo
        self.setStyleSheet("background-color: #92941e;")
        ## Permite usar enter para iniciar sesion
        self.volver_button.setStyleSheet("background-color: white;"
        "border-radius: 4px")
        self.label_titulo.setStyleSheet("font-weight: bold;"
        "font-size: 20pt")

        layout_vertical = QVBoxLayout()
        layout_vertical.addStretch(1)
        layout_vertical.addWidget(self.label_titulo)
        layout_vertical.addStretch(1)
        layout_vertical.addWidget(self.label_1)
        layout_vertical.addStretch(1)
        layout_vertical.addWidget(self.label_2)
        layout_vertical.addStretch(1)
        layout_vertical.addWidget(self.label_3)
        layout_vertical.addStretch(1)
        layout_vertical.addWidget(self.label_4)
        layout_vertical.addStretch(1)
        layout_vertical.addWidget(self.label_5)
        layout_vertical.addStretch(1)
        layout_vertical.addWidget(self.volver_button)
        layout_vertical.addStretch(1)

        h_main_layout = QHBoxLayout()
        h_main_layout.addStretch(1)
        h_main_layout.addLayout(layout_vertical)
        h_main_layout.addStretch(1)
        
        self.setLayout(h_main_layout)

    def volver(self):
        if self.senal_volver_inicio:
            self.senal_volver_inicio.emit()
            self.ocultar()

    def solicitar_jugadores(self):
        self.senal_solicitar_jugadores.emit()

    def recibir_jugadores(self, ranking_jugadores):

        if len(ranking_jugadores) == 1:
                self.label_1.setText(ranking_jugadores[0])

        elif len(ranking_jugadores) == 2:
            self.label_1.setText(ranking_jugadores[0])
            self.label_2.setText(ranking_jugadores[1])

        elif len(ranking_jugadores) == 3:
            self.label_1.setText(ranking_jugadores[0])
            self.label_2.setText(ranking_jugadores[1])
            self.label_3.setText(ranking_jugadores[2])
            
        elif len(ranking_jugadores) == 4:
            self.label_1.setText(ranking_jugadores[0])
            self.label_2.setText(ranking_jugadores[1])
            self.label_3.setText(ranking_jugadores[2])
            self.label_4.setText(ranking_jugadores[3])

        elif len(ranking_jugadores) >= 5:
            self.label_1.setText(ranking_jugadores[0])
            self.label_2.setText(ranking_jugadores[1])
            self.label_3.setText(ranking_jugadores[2])
            self.label_4.setText(ranking_jugadores[3])
            self.label_5.setText(ranking_jugadores[4])

        else:
            pass
            

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()

