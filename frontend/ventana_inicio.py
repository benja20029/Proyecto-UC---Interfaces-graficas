from PyQt5.QtCore  import pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap, QFont
import parametros as p 
## Se saca codigo de referencia de la AS3 (DCCobra)
class VentanaInicio(QWidget):

    senal_verificar_login = pyqtSignal(str)
    senal_ver_ranking = pyqtSignal()

    def __init__(self, tamano_ventana):
        super().__init__()
        self.inicio_ventana(tamano_ventana)

    def inicio_ventana(self, tamano_ventana):
        self.setWindowIcon(QIcon(p.RUTA_ICONO))
        ## """ A continuacion se configurara la geometria de la ventana. """
        self.setWindowTitle("Ventana de inicio")
        self.setGeometry(tamano_ventana)
        self.label_imagen = QLabel(self)
        self.label_usuario = QLabel("Escribe tu nombre de usuario: ", self)
        self.usuario_form = QLineEdit('', self)
        self.usuario_form.setGeometry(45,15, 200, 20)
        self.iniciar_button = QPushButton('Iniciar partida', self)
        self.iniciar_button.clicked.connect(self.enviar_login)
        self.ver_ranking_button = QPushButton("Ver ranking", self)
        self.ver_ranking_button.clicked.connect(self.ver_ranking)
    
        ##Estilo
        self.setStyleSheet("background-color: #92941e;")
        ## Permite usar enter para iniciar sesion
        self.usuario_form.returnPressed.connect(
           lambda: self.iniciar_button.click())
        self.iniciar_button.setStyleSheet("background-color: white;"
        "border-radius: 4px")
        self.ver_ranking_button.setStyleSheet("background-color: white;"
        "border-radius: 4px")
        self.usuario_form.setStyleSheet("background-color: white;"
        "border-radius: 4px")
        self.label_usuario.setStyleSheet("font-weight: bold")


        ## Se instancia imagen
        froggy = QPixmap(p.RUTA_LOGO)
        self.label_imagen.setPixmap(froggy)
        self.label_imagen.setMaximumSize(400, 400)
        self.label_imagen.setScaledContents(True)

        ## Layout horizontal que contiene el logo de Froggy
        primer_layout = QHBoxLayout()
        primer_layout.addStretch(1)
        primer_layout.addWidget(self.label_imagen)
        primer_layout.addStretch(1)

        segundo_layout = QVBoxLayout()
        segundo_layout.addStretch(1)
        segundo_layout.addWidget(self.iniciar_button)
        segundo_layout.addStretch(1)
        segundo_layout.addWidget(self.ver_ranking_button)
        segundo_layout.addStretch(1)

        tercer_layout = QHBoxLayout()
        tercer_layout.addWidget(self.label_usuario)
        tercer_layout.addWidget(self.usuario_form)

        cuarto_layout = QVBoxLayout()
        cuarto_layout.addStretch(1)
        cuarto_layout.addLayout(tercer_layout)
        cuarto_layout.addLayout(segundo_layout)
        cuarto_layout.addStretch(1)

        quinto_layout = QHBoxLayout()
        quinto_layout.addStretch(1)
        quinto_layout.addLayout(cuarto_layout)
        quinto_layout.addStretch(1)

        layout_final = QVBoxLayout()
        layout_final.addLayout(primer_layout)
        layout_final.addLayout(quinto_layout)

        self.setLayout(layout_final)

    def enviar_login(self):
        usuario = self.usuario_form.text()
        if self.senal_verificar_login:
            self.senal_verificar_login.emit(usuario)

    def recibir_validacion(self, respuesta):

        if respuesta[1]:
            self.ocultar()
        else:
            self.usuario_form.setText("")
            self.usuario_form.setPlaceholderText("Usuario invalido!")

    def ver_ranking(self):
        if self.senal_ver_ranking:
            self.senal_ver_ranking.emit()
            self.ocultar()

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()
