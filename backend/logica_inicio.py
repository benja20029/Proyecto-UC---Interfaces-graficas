from PyQt5.QtCore import QObject, pyqtSignal
import parametros as p

class LogicaInicio(QObject):

    senal_validacion = pyqtSignal(tuple)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, usuario: str):
        if usuario.isalnum() and len(usuario) >= p.MIN_CARACTERES and \
            len(usuario) <= p.MAX_CARACTERES:
            
            self.senal_abrir_juego.emit(usuario)
            self.senal_validacion.emit((usuario, True))

        else: 
            self.senal_validacion.emit((usuario, False))
        
