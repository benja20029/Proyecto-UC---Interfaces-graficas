import os
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QTimer, QRect
from PyQt5.QtWidgets import QLabel
import parametros as p
from time import sleep
from random import choice
import os
## Se toma como base el modulo logica_juego de AS3
class ThreadL(QThread):
    
    senal_actualizar_auto = pyqtSignal(int, int, str, int, str)
    senal_revisar_colision = pyqtSignal()
    def __init__(self, x, y, direccion, num_auto, tipo):
        super().__init__()
        self.x = x
        self.x_back_up = x
        self.y = y
        self.y_back_up = y
        self.direccion = direccion
        self.num_auto = num_auto
        self.pause = False
        self.tipo = tipo
        self.velocidad_troncos = p.VELOCIDAD_TRONCOS
        self.velocidad_autos = p.VELOCIDAD_AUTOS

    def run(self):
        while not self.pause:
            if self.tipo == "A":
                if self.x > -60:
                    self.x -= self.velocidad_autos
                    self.senal_actualizar_auto.emit(self.x, self.y, "L", self.num_auto, self.tipo)
                    sleep(p.TIEMPO_AVANCE)
                elif self.x <= -60 :
                    self.x = self.x_back_up
                    self.senal_actualizar_auto.emit(self.x, self.y, "L", self.num_auto, self.tipo)
                    sleep(p.TIEMPO_AUTOS)
            elif self.tipo == "T":
                if self.x > -60:
                    self.x -= self.velocidad_troncos
                    self.senal_actualizar_auto.emit(self.x, self.y, "L", self.num_auto, self.tipo)
                    sleep(p.TIEMPO_AVANCE)
                elif self.x <= -60 :
                    self.x = self.x_back_up
                    self.senal_actualizar_auto.emit(self.x, self.y, "L", self.num_auto, self.tipo)
                    sleep(p.TIEMPO_TRONCOS)

    def pasar_nivel(self):
        self.velocidad_troncos = self.velocidad_troncos * \
            ((2) / (1 + p.PONDERADOR_DIFICULTAD))
        self.velocidad_autos = self.velocidad_autos * \
            ((2) / (1 + p.PONDERADOR_DIFICULTAD))
        self.x = self.x_back_up
        self.y = self.y_back_up

class ThreadR(QThread):
    senal_actualizar_auto = pyqtSignal(int, int, str, int, str)
    senal_revisar_colision = pyqtSignal()
    def __init__(self, x, y, direccion, num_auto, tipo):
        super().__init__()
        self.x = x
        self.y = y
        self.x_back_up = x
        self.y_back_up = y
        self.direccion = direccion
        self.num_auto = num_auto
        self.pause = False
        self.tipo = tipo
        self.velocidad_troncos = p.VELOCIDAD_TRONCOS
        self.velocidad_autos = p.VELOCIDAD_AUTOS

    def run(self):
        while not self.pause:
            if self.tipo == "A":
                if self.x < 860:
                    self.x += self.velocidad_autos
                    self.senal_actualizar_auto.emit(self.x, self.y, "R", self.num_auto, self.tipo)
                    sleep(p.TIEMPO_AVANCE)
                elif self.x >= 860:
                    self.x = self.x_back_up
                    self.senal_actualizar_auto.emit(self.x, self.y, "R", self.num_auto, self.tipo)
                    sleep(p.TIEMPO_AUTOS)
            elif self.tipo == "T":
                if self.x < 860:
                    self.x += self.velocidad_troncos
                    self.senal_actualizar_auto.emit(self.x, self.y, "R", self.num_auto, self.tipo)
                    sleep(p.TIEMPO_AVANCE)
                elif self.x >= 860:
                    self.x = self.x_back_up
                    self.senal_actualizar_auto.emit(self.x, self.y, "R", self.num_auto, self.tipo)
                    sleep(p.TIEMPO_TRONCOS)
    def pasar_nivel(self):
        self.velocidad_troncos = self.velocidad_troncos * \
            ((2) / (1 + p.PONDERADOR_DIFICULTAD))
        self.velocidad_autos = self.velocidad_autos * \
            ((2) / (1 + p.PONDERADOR_DIFICULTAD))
        self.x = self.x_back_up
        self.y = self.y_back_up


class LogicaJuego(QObject):
    senal_post_nivel_derrota = pyqtSignal(int, int, int, int, int, str)
    senal_post_nivel_victoria = pyqtSignal(int, int, int, int, int, str)
    senal_actualizar_tiempo = pyqtSignal(str)
    senal_mov_froggy = pyqtSignal(tuple)
    senal_colision_ver = pyqtSignal(tuple)
    senal_cerrar_ventana_juego = pyqtSignal()
    senal_tocar_item = pyqtSignal(str, int)
    senal_aparecer_objeto = pyqtSignal(str, int, int)
    senal_actualizar_puntaje = pyqtSignal(int, int)
    
    def __init__(self):
        super().__init__()
        self.monedas = 0
        self.puntaje = 0
        self.puntaje_total = 0
        self.vidas = p.VIDAS_INICIO
        self.items_recolectados = 0
        self.duracion_ronda = p.DURACION_RONDA_INICIAL
        self.nivel = 1
        self.victoria = False
        self.instanciar_t_timer()
        self.instanciar_timer_objetos()
        self.pos_x_froggy = p.POS_X_FROGGY
        self.pos_y_froggy = p.POS_Y_FROGGY
        self.thread_auto_1_l = ThreadL(p.POS_X_AUTO_1_L, p.POS_Y_AUTO_1_L, "L", 0, "A")
        self.thread_auto_1_r = ThreadR(p.POS_X_AUTO_1_R, p.POS_Y_AUTO_1_R, "R", 0, "A")
        self.thread_auto_2_l = ThreadL(p.POS_X_AUTO_2_L, p.POS_Y_AUTO_2_L, "L", 1, "A")
        self.thread_auto_2_r = ThreadR(p.POS_X_AUTO_2_R, p.POS_Y_AUTO_2_R, "R", 1, "A")
        self.thread_auto_3_l = ThreadL(p.POS_X_AUTO_3_L, p.POS_Y_AUTO_3_L, "L", 2, "A")
        self.thread_auto_3_r = ThreadR(p.POS_X_AUTO_3_R, p.POS_Y_AUTO_3_R, "R", 2, "A")
        self.thread_auto_4_l = ThreadL(p.POS_X_AUTO_4_L, p.POS_Y_AUTO_4_L, "L", 3, "A")
        self.thread_auto_4_r = ThreadR(p.POS_X_AUTO_4_R, p.POS_Y_AUTO_4_R, "R", 3, "A")
        self.thread_auto_5_l = ThreadL(p.POS_X_AUTO_5_L, p.POS_Y_AUTO_5_L, "L", 4, "A")
        self.thread_auto_5_r = ThreadR(p.POS_X_AUTO_5_R, p.POS_Y_AUTO_5_R, "R", 4, "A")
        self.thread_auto_6_l = ThreadL(p.POS_X_AUTO_6_L, p.POS_Y_AUTO_6_L, "L", 5, "A")
        self.thread_auto_6_r = ThreadR(p.POS_X_AUTO_6_R, p.POS_Y_AUTO_6_R, "R", 5, "A")
        ## troncos
        self.thread_tronco_1_l = ThreadL(p.POS_X_TRONCO_1_L, p.POS_Y_TRONCO_1_L, "L", 0, "T")
        self.thread_tronco_1_r = ThreadR(p.POS_X_TRONCO_1_R, p.POS_Y_TRONCO_1_R, "R", 0, "T")
        self.thread_tronco_2_l = ThreadL(p.POS_X_TRONCO_2_L, p.POS_Y_TRONCO_2_L, "L", 1, "T")
        self.thread_tronco_2_r = ThreadR(p.POS_X_TRONCO_2_R, p.POS_Y_TRONCO_2_R, "R", 1, "T")
        self.thread_tronco_3_l = ThreadL(p.POS_X_TRONCO_3_L, p.POS_Y_TRONCO_3_L, "L", 2, "T")
        self.thread_tronco_3_r = ThreadR(p.POS_X_TRONCO_3_R, p.POS_Y_TRONCO_3_R, "R", 2, "T")
        ## Colocar posicion item
    def instanciar_timer_objetos(self):
        self.timer_objetos = QTimer()
        self.timer_objetos.timeout.connect(self.sub_tick_objetos)
        self.timer_objetos.setInterval(p.TIEMPO_OBJETO * 1000)

    def instanciar_t_timer(self):
        self.t_timer = QTimer()
        self.t_timer.timeout.connect(self.t_timer_tick)
        self.tiempo = self.duracion_ronda
        self.t_timer.setInterval(1000)

    def sub_tick_objetos(self):
        lista_objetos = ["Calavera", "Corazon", "Moneda", "Reloj"]
        objeto_elegido = choice(lista_objetos)
        pos_x = [i for i in range(20, 780)]
        pos_y_1 = [i for i in range(200, 300)]
        pos_y_2 = [i for i in range(450, 650)]
        x_objeto = choice(pos_x)
        y_tentativas = [pos_y_1, pos_y_2]
        y_posiciones = choice(y_tentativas)
        y_objeto = choice(y_posiciones)
        self.senal_aparecer_objeto.emit(objeto_elegido, x_objeto, y_objeto)

    def revision_mov_froggy(self, direccion):
        if direccion == "U":
            self.pos_y_froggy -= p.VELOCIDAD_CAMINAR
        elif direccion == "D":
            self.pos_y_froggy += p.VELOCIDAD_CAMINAR
        elif direccion == "R":
            self.pos_x_froggy += p.VELOCIDAD_CAMINAR
        elif direccion == "L":
            self.pos_x_froggy -= p.VELOCIDAD_CAMINAR
        self.pos_x_froggy, self.pos_y_froggy = self.colision_bordes(\
            self.pos_x_froggy, self.pos_y_froggy)
        self.senal_mov_froggy.emit((self.pos_x_froggy, self.pos_y_froggy))

    def iniciar_juego(self):
        self.t_timer.start()
        self.timer_objetos.start()
        #Autos
        self.auto_hilera_1 = [self.thread_auto_1_l, self.thread_auto_1_r]
        self.auto_hilera_2 = [self.thread_auto_2_l, self.thread_auto_2_r]
        self.auto_hilera_3 = [self.thread_auto_3_l, self.thread_auto_3_r]
        self.auto_hilera_4 = [self.thread_auto_4_l, self.thread_auto_4_r]
        self.auto_hilera_5 = [self.thread_auto_5_l, self.thread_auto_5_r]
        self.auto_hilera_6 = [self.thread_auto_6_l, self.thread_auto_6_r]
        self.thread_auto_hilera_1 = choice(self.auto_hilera_1)
        self.thread_auto_hilera_2 = choice(self.auto_hilera_2)
        self.thread_auto_hilera_3 = choice(self.auto_hilera_3)
        self.thread_auto_hilera_4 = choice(self.auto_hilera_4)
        self.thread_auto_hilera_5 = choice(self.auto_hilera_5)
        self.thread_auto_hilera_6 = choice(self.auto_hilera_6)
        ## Troncos
        self.tronco_hilera_1 = [self.thread_tronco_1_l, self.thread_tronco_1_r]
        self.tronco_hilera_2 = [self.thread_tronco_2_l, self.thread_tronco_2_r]
        self.tronco_hilera_3 = [self.thread_tronco_3_l, self.thread_tronco_3_r]
        self.thread_tronco_hilera_1 = choice(self.tronco_hilera_1)
        if self.thread_tronco_hilera_1 == self.thread_tronco_1_l:
            self.thread_tronco_hilera_2 = self.tronco_hilera_2[1]
            self.thread_tronco_hilera_3 = self.tronco_hilera_3[0]
        elif self.thread_tronco_hilera_1 == self.thread_tronco_1_r:
            self.thread_tronco_hilera_2 = self.tronco_hilera_2[0]
            self.thread_tronco_hilera_3 = self.tronco_hilera_3[1]
        self.timer_movimiento_objetos= QTimer()
        self.timer_movimiento_objetos.timeout.connect(self.sub_tick_mov)
        self.auto = 0
        self.timer_movimiento_objetos.setInterval(100)
        self.thread_auto_hilera_1.pause = False
        self.thread_auto_hilera_2.pause = False
        self.thread_auto_hilera_3.pause = False
        self.thread_auto_hilera_4.pause = False
        self.thread_auto_hilera_5.pause = False
        self.thread_auto_hilera_6.pause = False
        self.thread_tronco_hilera_1.pause = False
        self.thread_tronco_hilera_2.pause = False
        self.thread_tronco_hilera_3.pause = False
        self.timer_movimiento_objetos.start()
    
    def sub_tick_mov(self):
        if self.auto == 0:
            self.thread_auto_hilera_1.start()
            self.thread_tronco_hilera_1.start()
            self.auto += 1
        elif self.auto == 1:
            self.thread_auto_hilera_2.start()
            self.thread_tronco_hilera_2.start()
            self.auto += 1
        elif self.auto == 2:
            self.thread_auto_hilera_3.start()  
            self.auto += 1
        elif self.auto == 3:
            self.thread_auto_hilera_4.start()
            self.auto += 1
        elif self.auto == 4:
            self.thread_auto_hilera_5.start()
            self.auto += 1
        elif self.auto == 5:
            self.thread_auto_hilera_6.start()
            self.thread_tronco_hilera_3.start()
            self.auto += 1
        elif self.auto == 6:
            self.timer_movimiento_objetos.stop()

    def detener_juego(self):
        self.t_timer.stop()
        self.timer_objetos.stop()
        self.thread_auto_hilera_1.pause = True
        self.thread_auto_hilera_2.pause = True
        self.thread_auto_hilera_3.pause = True
        self.thread_auto_hilera_4.pause = True
        self.thread_auto_hilera_5.pause = True
        self.thread_auto_hilera_6.pause = True
        self.thread_tronco_hilera_1.pause = True
        self.thread_tronco_hilera_2.pause = True
        self.thread_tronco_hilera_3.pause = True

    def reanudar_juego(self):
        self.t_timer.start()
        self.timer_objetos.start()
        self.thread_auto_hilera_1.pause = False
        self.thread_auto_hilera_2.pause = False
        self.thread_auto_hilera_3.pause = False
        self.thread_auto_hilera_4.pause = False
        self.thread_auto_hilera_5.pause = False
        self.thread_auto_hilera_6.pause = False
        self.thread_tronco_hilera_1.pause = False
        self.thread_tronco_hilera_2.pause = False
        self.thread_tronco_hilera_3.pause = False
        self.thread_auto_hilera_1.start()
        self.thread_auto_hilera_2.start()
        self.thread_auto_hilera_3.start()
        self.thread_auto_hilera_4.start()
        self.thread_auto_hilera_5.start()
        self.thread_auto_hilera_6.start()
        self.thread_tronco_hilera_1.start()
        self.thread_tronco_hilera_2.start()
        self.thread_tronco_hilera_3.start()

    def t_timer_tick(self):
        if self.tiempo > 0:
            self.tiempo -= 1
        else:
            self.tiempo = 0
        if self.vidas == 0 or self.tiempo == 0 or self.victoria:
            self.puntaje = (((self.vidas * 100) + (self.tiempo * 50)) * self.nivel)
            self.puntaje_total += self.puntaje
            self.senal_cerrar_ventana_juego.emit() ## Cierra la ventana de juego
            if self.vidas == 0 or self.tiempo == 0:
                self.senal_post_nivel_derrota.emit(self.nivel, self.puntaje_total, 
                self.puntaje, self.vidas, self.monedas, self.usuario)
                self.senal_cerrar_ventana_juego.emit()
                self.detener_juego()
            elif self.victoria:
                self.senal_post_nivel_victoria.emit(self.nivel, self.puntaje_total, 
                self.puntaje, self.vidas, self.monedas, self.usuario)
                self.senal_cerrar_ventana_juego.emit()
                self.victoria = False
                self.pos_x_froggy = p.POS_X_FROGGY
                self.pos_y_froggy = p.POS_Y_FROGGY
                self.nivel += 1
                self.senal_actualizar_puntaje.emit(self.nivel, self.puntaje_total)
                self.detener_juego()

        self.senal_actualizar_tiempo.emit(str(self.tiempo))

    def colision_objetos(self, froggy: QLabel, objeto_2: QLabel, posx_tronco, posy_tronco, 
    tipo: str, usuario: str, puntaje: int, tipo_item: str):
        self.usuario = usuario
        froggy_rect = froggy.geometry()
        objeto_2_rect = objeto_2.geometry()
        interseccion = froggy_rect.intersects(objeto_2_rect)
        if interseccion:
            if tipo == "R" or tipo == "A":
                self.pos_x_froggy = p.POS_X_FROGGY
                self.pos_y_froggy = p.POS_Y_FROGGY
                self.senal_colision_ver.emit((self.pos_x_froggy, self.pos_y_froggy, True))
                self.vidas -= 1
                interseccion = False
            elif tipo == "T":
                self.pos_x_froggy = posx_tronco
                self.pos_y_froggy = posy_tronco
                self.senal_colision_ver.emit((self.pos_x_froggy, self.pos_y_froggy, False))
                interseccion = False

            elif tipo == "V":
                self.victoria = True

            elif tipo == "I":
                if tipo_item == "CA":
                    p.VELOCIDAD_TRONCOS *= 1.05
                    self.senal_tocar_item.emit("Calavera", 0)
                elif tipo_item == "CO":
                    self.vidas += 1
                    self.senal_tocar_item.emit("Corazon", self.vidas)
                elif tipo_item == "M":
                    self.monedas += p.CANTIDAD_MONEDAS
                    self.senal_tocar_item.emit("Moneda", self.monedas)
                elif tipo_item == "R":
                    self.tiempo_adicional = 10 * (self.tiempo / p.DURACION_RONDA_INICIAL)
                    self.tiempo += self.tiempo_adicional
                    self.tiempo = round(self.tiempo)
                    self.senal_actualizar_tiempo.emit(str(self.tiempo))
                    self.senal_tocar_item.emit("Reloj", 0)

    def colision_bordes(self, x, y):
        
        if x > p.MAX_X:
            nueva_x = p.MAX_X
            return (nueva_x, y)

        elif x < p.MIN_X:
            nueva_x = p.MIN_X
            return (nueva_x, y)

        elif y > p.MAX_Y:
            nueva_y = p.MAX_Y
            return (x, nueva_y)

        elif y < p.MIN_Y:
            nueva_y = p.MIN_Y
            return (x, nueva_y)

        else:
            return (x, y)

    def pasar_nivel(self):
        self.duracion_ronda = p.PONDERADOR_DIFICULTAD * self.duracion_ronda
        self.tiempo = round(self.duracion_ronda)
        