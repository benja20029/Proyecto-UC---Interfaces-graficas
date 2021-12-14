from PyQt5.QtCore  import pyqtSignal, QRect
from PyQt5.QtWidgets import QLabel, QMessageBox, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5 import uic
import parametros as p 
#Se importa bosquejo de ventana de Qt Designer
## Se utiliza ventana juego de AS3 como ejemplo para este modulo
nombre_ventana, clase_base = uic.loadUiType(p.RUTA_UI_VENTANA_JUEGO)
class VentanaJuego(nombre_ventana, clase_base):
    senal_iniciar_juego = pyqtSignal()
    senal_tecla = pyqtSignal(str)
    senal_pausa = pyqtSignal()
    senal_timer = pyqtSignal()
    senal_parar_t_timer = pyqtSignal()
    senal_verificar_colision = pyqtSignal(QLabel, QLabel, int, int, str, str, int, str)
    senal_reanudar_juego = pyqtSignal()
    senal_froggy_tronco = pyqtSignal(QLabel, QLabel, int, int, str, str, int, str)
    senal_aparicion_items = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        self.contador = 0

    def mostrar_ventana(self, usuario):
        if self.contador == 0:
            self.casilla_puntaje.setText("0")
            self.casilla_nivel.setText("1")
            self.vidas = p.VIDAS_INICIO
            self.casilla_vidas.setText(f"{self.vidas}")
            self.casilla_monedas.setText("0")
            self.contador += 1
        self.show()
        self.tipo_item = ""
        self.senal_iniciar_juego.emit()
        self.senal_timer.emit()
        self.usuario = usuario
        self.pausa = False
        self.senal_aparicion_items.emit()
        
    def keyPressEvent(self, event):
        if event.text().lower() == p.TECLA_ARRIBA:
            self.senal_tecla.emit("U")
            self.sprite_froggy_u = QPixmap(p.RUTA_FROGGY_UP)
            self.label_froggy.setPixmap(self.sprite_froggy_u)
        elif event.text().lower() == p.TECLA_ABAJO:
            self.senal_tecla.emit("D")
            self.sprite_froggy_d = QPixmap(p.RUTA_FROGGY_DOWN)
            self.label_froggy.setPixmap(self.sprite_froggy_d)
        elif event.text().lower() == p.TECLA_DERECHA:
            self.senal_tecla.emit("R")
            self.sprite_froggy_r = QPixmap(p.RUTA_FROGGY_RIGHT)
            self.label_froggy.setPixmap(self.sprite_froggy_r)
        elif event.text().lower() == p.TECLA_IZQUIERDA:
            self.senal_tecla.emit("L")
            self.sprite_froggy_l = QPixmap(p.RUTA_FROGGY_LEFT)
            self.label_froggy.setPixmap(self.sprite_froggy_l)
        elif event.text().lower() == p.TECLA_PAUSA:
            self.senal_pausa.emit()
        self.label_froggy.setScaledContents(True)

    def init_gui(self):
        self.setWindowIcon(QIcon(p.RUTA_ICONO))
        self.casilla_tiempo.setText(f"{p.DURACION_RONDA_INICIAL}")
        ## "Se configura la ventana a continuacion" ##
        self.setWindowTitle("Ventana de juego")
        self.imagen = QPixmap(p.RUTA_LOGO)
        self.imagen_pasto = QPixmap(p.RUTA_PASTO)
        self.logo_froggy.setPixmap(self.imagen)
        self.logo_froggy.setScaledContents(True)
        self.fondo_juego.setPixmap(self.imagen_pasto)
        self.fondo_juego.setScaledContents(True)
        ## Desarrollo boton de pausa
        self.mensaje_pausa = QMessageBox()
        label_pausa = QLabel()
        label_pausa.setText("Pausaste el juego")
        label_pausa.setFont(QFont("Times", 20))
        self.label_froggy = QLabel(self)
        self.imagen_pausa = QPixmap(p.RUTA_FROGGY_PAUSE)
        self.label_froggy.setPixmap(self.imagen_pausa)
        self.label_froggy.setScaledContents(True)
        self.label_froggy.setMaximumSize(60, 80)
        self.mensaje_pausa.layout().setGeometry(QRect(80, 320, 300, 100))
        self.mensaje_pausa.layout().addWidget(self.label_froggy)
        self.mensaje_pausa.setStandardButtons(QMessageBox.Close)
        self.mensaje_pausa.layout().addWidget(label_pausa)
        self.mensaje_pausa.setWindowTitle("Menu de pausa")
        self.mensaje_pausa.buttonClicked.connect(self.mostrar_pausa)
        self.mensaje_pausa.setWindowIcon(QIcon(p.RUTA_ICONO))
        self.pause_button.clicked.connect(self.mostrar_pausa)
        self.exit_button.clicked.connect(self.salir)
        self.senal_pausa.connect(self.mostrar_pausa)
        ## Falta corregir boton de pausa
        ## COMPLETAR
        ## Carretera 1 (Desde abajo hacia arriba)
        self.label_carretera_1 = QLabel("", self)
        self.sprite_carretera = QPixmap(p.RUTA_CARRETERA)
        self.label_carretera_1.setPixmap(self.sprite_carretera)
        self.label_carretera_1.setScaledContents(True)
        self.label_carretera_1.setGeometry(0, 500, 800, 100)
        ## Rio
        self.label_rio = QLabel("", self)
        self.sprite_rio = QPixmap(p.RUTA_RIO)
        self.label_rio.setPixmap(self.sprite_rio)
        self.label_rio.setScaledContents(True)
        self.label_rio.setGeometry(0, 350, 800, 100)
        ## Carretera 2
        self.label_carretera_2 = QLabel("", self)
        self.label_carretera_2.setPixmap(self.sprite_carretera)
        self.label_carretera_2.setScaledContents(True)
        self.label_carretera_2.setGeometry(0, 200, 800, 100)
        ## Auto rojo ultima fila
        # Va hacia la izquierda
        self.label_auto_1_l = QLabel("", self)
        self.sprite_auto_1_l = QPixmap(p.RUTA_AUTO_ROJO_L)
        self.label_auto_1_l.setPixmap(self.sprite_auto_1_l)
        self.label_auto_1_l.setScaledContents(True)
        self.label_auto_1_l.setGeometry(p.POS_X_AUTO_1_L, p.POS_Y_AUTO_1_L, 60, 25)
        # Va hacia la derecha
        self.label_auto_1_r = QLabel("", self)
        self.sprite_auto_1_r = QPixmap(p.RUTA_AUTO_ROJO_R)
        self.label_auto_1_r.setPixmap(self.sprite_auto_1_r)
        self.label_auto_1_r.setScaledContents(True)
        self.label_auto_1_r.setGeometry(p.POS_X_AUTO_1_R, p.POS_Y_AUTO_1_R, 60, 25)
        ## Auto plata penultima fila
        #Va hacia la izquierda
        self.label_auto_2_l = QLabel("", self)
        self.sprite_auto_2_l = QPixmap(p.RUTA_AUTO_PLATA_L)
        self.label_auto_2_l.setPixmap(self.sprite_auto_2_l)
        self.label_auto_2_l.setScaledContents(True)
        self.label_auto_2_l.setGeometry(p.POS_X_AUTO_2_L, p.POS_Y_AUTO_2_L, 60, 25)
        #Va hacia la derecha
        self.label_auto_2_r = QLabel("", self)
        self.sprite_auto_2_r = QPixmap(p.RUTA_AUTO_PLATA_R)
        self.label_auto_2_r.setPixmap(self.sprite_auto_2_r)
        self.label_auto_2_r.setScaledContents(True)
        self.label_auto_2_r.setGeometry(p.POS_X_AUTO_2_R, p.POS_Y_AUTO_2_R, 60, 25)
        ## Auto Blanco 3ra fila desde abajo hacia arriba
        #Va hacia la izquierda
        self.label_auto_3_l = QLabel("", self)
        self.sprite_auto_3_l = QPixmap(p.RUTA_AUTO_BLANCO_L)
        self.label_auto_3_l.setPixmap(self.sprite_auto_3_l)
        self.label_auto_3_l.setScaledContents(True)
        self.label_auto_3_l.setGeometry(p.POS_X_AUTO_3_L, p.POS_Y_AUTO_3_L, 60, 25)
        # Va hacia la derecha
        self.label_auto_3_r = QLabel("", self)
        self.sprite_auto_3_r = QPixmap(p.RUTA_AUTO_BLANCO_R)
        self.label_auto_3_r.setPixmap(self.sprite_auto_3_r)
        self.label_auto_3_r.setScaledContents(True)
        self.label_auto_3_r.setGeometry(p.POS_X_AUTO_3_R, p.POS_Y_AUTO_3_R, 60, 25)
        ## Auto negro 4ta fila desde abajo hacia arriba
        # Va hacia la izquierda
        self.label_auto_4_l = QLabel("", self)
        self.sprite_auto_4_l = QPixmap(p.RUTA_AUTO_NEGRO_L)
        self.label_auto_4_l.setPixmap(self.sprite_auto_4_l)
        self.label_auto_4_l.setScaledContents(True)
        self.label_auto_4_l.setGeometry(p.POS_X_AUTO_4_L, p.POS_Y_AUTO_4_L, 60, 25)
        # Va hacia la derecha
        self.label_auto_4_r = QLabel("", self)
        self.sprite_auto_4_r = QPixmap(p.RUTA_AUTO_NEGRO_R)
        self.label_auto_4_r.setPixmap(self.sprite_auto_4_r)
        self.label_auto_4_r.setScaledContents(True)
        self.label_auto_4_r.setGeometry(p.POS_X_AUTO_4_R, p.POS_Y_AUTO_4_R, 60, 25)
        # Auto morado 5ta fila desde abajo hacia arriba
        # Va hacia la izquierda
        self.label_auto_5_l = QLabel("", self)
        self.sprite_auto_5_l = QPixmap(p.RUTA_AUTO_MORADO_L)
        self.label_auto_5_l.setPixmap(self.sprite_auto_5_l)
        self.label_auto_5_l.setScaledContents(True)
        self.label_auto_5_l.setGeometry(p.POS_X_AUTO_5_L, p.POS_Y_AUTO_5_L, 60, 25)
        # Va hacia la derecha
        self.label_auto_5_r = QLabel("", self)
        self.sprite_auto_5_r = QPixmap(p.RUTA_AUTO_MORADO_R)
        self.label_auto_5_r.setPixmap(self.sprite_auto_5_r)
        self.label_auto_5_r.setScaledContents(True)
        self.label_auto_5_r.setGeometry(p.POS_X_AUTO_5_R, p.POS_Y_AUTO_5_R, 60, 25)
        # Auto azul 6ta fila desde abajo hacia arriba
        # Va hacia la izquierda
        self.label_auto_6_l = QLabel("", self)
        self.sprite_auto_6_l = QPixmap(p.RUTA_AUTO_AZUL_L)
        self.label_auto_6_l.setPixmap(self.sprite_auto_6_l)
        self.label_auto_6_l.setScaledContents(True)
        self.label_auto_6_l.setGeometry(p.POS_X_AUTO_6_L, p.POS_Y_AUTO_6_L, 60, 25)
        #Va hacia la derecha
        self.label_auto_6_r = QLabel("", self)
        self.sprite_auto_6_r = QPixmap(p.RUTA_AUTO_AZUL_R)
        self.label_auto_6_r.setPixmap(self.sprite_auto_6_r)
        self.label_auto_6_r.setScaledContents(True)
        self.label_auto_6_r.setGeometry(p.POS_X_AUTO_6_R, p.POS_Y_AUTO_6_R, 60, 25)   
        ## Troncos
        # Tronco Hilera 1 (Desde abajo hacia arriba)
        # Va hacia la izquierda
        self.label_tronco_1_l = QLabel("", self)
        self.sprite_tronco = QPixmap(p.RUTA_TRONCO)
        self.label_tronco_1_l.setPixmap(self.sprite_tronco)
        self.label_tronco_1_l.setScaledContents(True)
        self.label_tronco_1_l.setGeometry(p.POS_X_TRONCO_1_L, p.POS_Y_TRONCO_1_L, 60, 25)
        # Va hacia la derecha
        self.label_tronco_1_r = QLabel("", self)
        self.label_tronco_1_r.setPixmap(self.sprite_tronco)
        self.label_tronco_1_r.setScaledContents(True)
        self.label_tronco_1_r.setGeometry(p.POS_X_TRONCO_1_R, p.POS_Y_TRONCO_1_R, 60, 25)
        # Tronco hilera 2
        # Va hacia la izquierda
        self.label_tronco_2_l = QLabel("", self)
        self.label_tronco_2_l.setPixmap(self.sprite_tronco)
        self.label_tronco_2_l.setScaledContents(True)
        self.label_tronco_2_l.setGeometry(p.POS_X_TRONCO_2_L, p.POS_Y_TRONCO_2_L, 60, 25)
        # Va hacia la derecha
        self.label_tronco_2_r = QLabel("", self)
        self.label_tronco_2_r.setPixmap(self.sprite_tronco)
        self.label_tronco_2_r.setScaledContents(True)
        self.label_tronco_2_r.setGeometry(p.POS_X_TRONCO_2_R, p.POS_Y_TRONCO_2_R, 60, 25)
        # Tronco hilera 3
        # Va hacia la izquierda
        self.label_tronco_3_l = QLabel("", self)
        self.label_tronco_3_l.setPixmap(self.sprite_tronco)
        self.label_tronco_3_l.setScaledContents(True)
        self.label_tronco_3_l.setGeometry(p.POS_X_TRONCO_3_L, p.POS_Y_TRONCO_3_L, 60, 25)
        # Va hacia la derecha
        self.label_tronco_3_r = QLabel("", self)
        self.label_tronco_3_r.setPixmap(self.sprite_tronco)
        self.label_tronco_3_r.setScaledContents(True)
        self.label_tronco_3_r.setGeometry(p.POS_X_TRONCO_3_R, p.POS_Y_TRONCO_3_R, 60, 25)
        # Pasto victoria
        self.label_victoria = QLabel("", self)
        self.label_victoria.setPixmap(self.imagen_pasto)
        self.label_victoria.setScaledContents(True)
        self.label_victoria.setGeometry(0, 150, 800, 50)
        self.label_victoria.raise_()
        ## Items
        self.label_calavera = QLabel("", self) ## CALAVERA
        self.sprite_calavera = QPixmap(p.RUTA_CALAVERA)
        self.label_calavera.setPixmap(self.sprite_calavera)
        self.label_calavera.setScaledContents(True)
        self.label_calavera.setGeometry(-60, 350, 30, 30)
        #################
        self.label_corazon = QLabel("", self) ## Corazon
        self.sprite_corazon = QPixmap(p.RUTA_CORAZON)
        self.label_corazon.setPixmap(self.sprite_corazon)
        self.label_corazon.setScaledContents(True)
        self.label_corazon.setGeometry(-60, 270, 30, 30)
        #################
        self.label_moneda = QLabel("", self) ## Moneda
        self.sprite_moneda = QPixmap(p.RUTA_MONEDA)
        self.label_moneda.setPixmap(self.sprite_moneda)
        self.label_moneda.setScaledContents(True)
        self.label_moneda.setGeometry(-60, 310, 30, 30)
        #################
        self.label_reloj = QLabel("", self) ## Reloj
        self.sprite_reloj = QPixmap(p.RUTA_RELOJ)
        self.label_reloj.setPixmap(self.sprite_reloj)
        self.label_reloj.setScaledContents(True)
        self.label_reloj.setGeometry(-60, 350, 30, 30)
        ## Insercion Froggy en el juego
        self.init_froggy()

    def init_froggy(self):
        self.label_froggy = QLabel("", self)
        self.sprite_froggy = QPixmap(p.RUTA_FROGGY_STILL)
        self.label_froggy.setPixmap(self.sprite_froggy)
        self.label_froggy.setScaledContents(True)
        self.label_froggy.setGeometry(p.POS_X_FROGGY, p.POS_Y_FROGGY, 30, 30)
        self.label_froggy.raise_()

    def move_froggy(self, pos):
        x, y = pos
        self.label_froggy.move(x, y)
        self.labels_autos = [self.label_auto_1_l, self.label_auto_1_r, self.label_auto_2_l, 
        self.label_auto_2_r, self.label_auto_2_r, self.label_auto_3_l, self.label_auto_3_r, 
        self.label_auto_4_l, self.label_auto_4_r, self.label_auto_5_l, self.label_auto_5_r, 
        self.label_auto_6_l, self.label_auto_6_r]
        self.labels_items = [(self.label_moneda, "M"), (self.label_reloj, "R"), 
        (self.label_calavera, "CA"), (self.label_corazon, "CO")]
        for auto in self.labels_autos:
            self.senal_verificar_colision.emit(self.label_froggy, auto, x, y, "A", 
            self.usuario, self.puntaje, self.tipo_item)

        for item, tipo_item in self.labels_items:
            self.senal_verificar_colision.emit(self.label_froggy, item, x, y, "I", 
            self.usuario, self.puntaje, tipo_item)
        ##self.senal_verificar_colision.emit(self.label_froggy, self.label_rio, x, y, "R")
        self.senal_verificar_colision.emit(self.label_froggy, self.label_victoria, x, y, "V", 
        self.usuario, self.puntaje, self.tipo_item)

    def colision_verificada(self, tuple: tuple):
        x, y, pierde_vida = tuple
        self.label_froggy.move(x, y)
        if pierde_vida:
            self.vidas -= 1
            self.casilla_vidas.setText(f"{self.vidas}")
            ##if self.vidas == 0:
              ##  self.salir()
      
    def mover_objeto(self, x, y, direccion, num_objeto, tipo):
        autos_izquierda = [self.label_auto_1_l, self.label_auto_2_l, self.label_auto_3_l, 
        self.label_auto_4_l, self.label_auto_5_l, self.label_auto_6_l]
        autos_derecha = [self.label_auto_1_r, self.label_auto_2_r, self.label_auto_3_r, 
        self.label_auto_4_r, self.label_auto_5_r, self.label_auto_6_r]
        troncos_izquierda = [self.label_tronco_1_l, self.label_tronco_2_l, self.label_tronco_3_l]
        troncos_derecha = [self.label_tronco_1_r, self.label_tronco_2_r, self.label_tronco_3_r]
        if tipo == "A":
            if direccion == "R":
                autos_derecha[num_objeto].move(x, y)
                self.senal_verificar_colision.emit(self.label_froggy, autos_derecha[num_objeto], 
                x, y, "A", self.usuario, self.puntaje, self.tipo_item)
            elif direccion == "L":
                autos_izquierda[num_objeto].move(x, y)  
                self.senal_verificar_colision.emit(self.label_froggy, autos_izquierda[num_objeto], 
                x, y, "A", self.usuario, self.puntaje, self.tipo_item)
        elif tipo == "T":
            if direccion == "R":
                troncos_derecha[num_objeto].move(x, y)
                self.senal_froggy_tronco.emit(self.label_froggy, troncos_derecha[num_objeto], 
                x, y, "T", self.usuario, self.puntaje, self.tipo_item)

            elif direccion == "L":
                troncos_izquierda[num_objeto].move(x, y)
                self.senal_froggy_tronco.emit(self.label_froggy, troncos_izquierda[num_objeto], 
                x, y, "T", self.usuario, self.puntaje, self.tipo_item)

    def salir(self):
        self.close()

    def mostrar_pausa(self):
        if self.pausa:
            self.mensaje_pausa.hide()
            self.senal_reanudar_juego.emit()
            self.pausa = False
        else:
            self.mensaje_pausa.show()
            self.senal_parar_t_timer.emit()
            self.pausa = True

    def esconder_menu_pausa(self):
        self.mensaje_pausa.hide()

    def set_time(self, tiempo):
        self.casilla_tiempo.setText(tiempo)
        

    def aparicion_items(self, objeto, x_objeto, y_objeto):
        if objeto == "Moneda":
            self.label_moneda.setGeometry(x_objeto, y_objeto, 30, 30)
        elif objeto == "Calavera":
            self.label_calavera.setGeometry(x_objeto, y_objeto, 30, 30)
        elif objeto == "Reloj":
            self.label_reloj.setGeometry(x_objeto, y_objeto, 30, 30)
        elif objeto == "Corazon":
            self.label_corazon.setGeometry(x_objeto, y_objeto, 30, 30)

    def item_tocado(self, tipo, variable):
        if tipo == "Corazon":
            self.casilla_vidas.setText(f"{variable}")
            self.label_corazon.setGeometry(-60, 200, 30, 30)
        elif tipo == "Moneda":
            self.casilla_monedas.setText(f"{variable}")
            self.label_moneda.setGeometry(-60, 200, 30, 30)
        elif tipo == "Calavera":
            self.label_calavera.setGeometry(-60, 200, 30, 30)
        elif tipo == "Reloj":
            self.label_reloj.setGeometry(-60, 200, 30, 30)

    def set_geometrias(self):
        self.label_auto_1_l.setGeometry(p.POS_X_AUTO_1_L, p.POS_Y_AUTO_1_L, 60, 25)
        self.label_auto_1_r.setGeometry(p.POS_X_AUTO_1_R, p.POS_Y_AUTO_1_R, 60, 25)
        self.label_auto_2_l.setGeometry(p.POS_X_AUTO_2_L, p.POS_Y_AUTO_2_L, 60, 25)
        self.label_auto_2_r.setGeometry(p.POS_X_AUTO_2_R, p.POS_Y_AUTO_2_R, 60, 25)
        self.label_auto_3_l.setGeometry(p.POS_X_AUTO_3_L, p.POS_Y_AUTO_3_L, 60, 25)
        self.label_auto_3_r.setGeometry(p.POS_X_AUTO_3_R, p.POS_Y_AUTO_3_R, 60, 25)
        self.label_auto_4_l.setGeometry(p.POS_X_AUTO_4_L, p.POS_Y_AUTO_4_L, 60, 25)
        self.label_auto_4_r.setGeometry(p.POS_X_AUTO_4_L, p.POS_Y_AUTO_4_L, 60, 25)
        self.label_auto_5_l.setGeometry(p.POS_X_AUTO_5_L, p.POS_Y_AUTO_5_L, 60, 25)
        self.label_auto_5_r.setGeometry(p.POS_X_AUTO_5_L, p.POS_Y_AUTO_5_L, 60, 25)
        self.label_auto_6_l.setGeometry(p.POS_X_AUTO_6_L, p.POS_Y_AUTO_6_L, 60, 25)
        self.label_auto_6_r.setGeometry(p.POS_X_AUTO_6_R, p.POS_Y_AUTO_6_R, 60, 25)
        self.label_tronco_1_l.setGeometry(p.POS_X_TRONCO_1_L, p.POS_Y_TRONCO_1_L, 60, 25)
        self.label_tronco_1_r.setGeometry(p.POS_X_TRONCO_1_R, p.POS_Y_TRONCO_1_R, 60, 25)
        self.label_tronco_2_l.setGeometry(p.POS_X_TRONCO_2_L, p.POS_Y_TRONCO_2_L, 60, 25)
        self.label_tronco_2_r.setGeometry(p.POS_X_TRONCO_2_R, p.POS_Y_TRONCO_2_R, 60, 25)
        self.label_tronco_3_l.setGeometry(p.POS_X_TRONCO_3_L, p.POS_Y_TRONCO_3_L, 60, 25)
        self.label_tronco_3_r.setGeometry(p.POS_X_TRONCO_3_R, p.POS_Y_TRONCO_3_R, 60, 25)
        self.label_calavera.setGeometry(-60, 350, 30, 30)
        self.label_corazon.setGeometry(-60, 270, 30, 30)
        self.label_moneda.setGeometry(-60, 310, 30, 30)
        self.label_reloj.setGeometry(-60, 350, 30, 30)
        self.label_froggy.setGeometry(p.POS_X_FROGGY, p.POS_Y_FROGGY, 30, 30)

    def nivel_puntaje(self, nivel, puntaje):
        self.puntaje = puntaje
        self.nivel = nivel
        self.casilla_nivel.setText(str(self.nivel))
        self.casilla_puntaje.setText(str(self.puntaje))