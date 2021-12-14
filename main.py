import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication
from backend.logica_inicio import LogicaInicio
from backend.logica_ranking import LogicaRanking
from backend.logica_juego import LogicaJuego
from backend.logica_post_nivel import LogicaPostNivel
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_ranking import VentanaRanking
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_post_nivel  import VentanaPostNivel

import parametros as p


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ == hook

    app = QApplication([])
    app.setApplicationName("DCCrossy Frog")

    ## Instanciacion ventana
    tamano_ventana = QRect(*p.TAMAÑO_VENTANA)
    #Inicio
    ventana_inicio = VentanaInicio(tamano_ventana)
    logica_inicio = LogicaInicio()

    # Ranking
    ventana_ranking = VentanaRanking(tamano_ventana)
    logica_ranking = LogicaRanking()

    # Juego
    ventana_juego = VentanaJuego()
    logica_juego = LogicaJuego()

    # Post nivel
    ventana_post_nivel = VentanaPostNivel()
    logica_post_nivel = LogicaPostNivel()
    #### Conexion señales
    ###
    
    ## Inicio --> **
    # Ventana inicio --> Logica inicio
    ventana_inicio.senal_verificar_login.connect(\
        logica_inicio.comprobar_usuario)

    # Ventana inicio --> Ventana Ranking
    ventana_inicio.senal_ver_ranking.connect(\
        ventana_ranking.mostrar)
    # Ventana inicio --> Logica Ranking
    ventana_inicio.senal_ver_ranking.connect(\
        logica_ranking.enviar_jugadores)

    ## Ventana inicio --> Ventana juego
    logica_inicio.senal_abrir_juego.connect(\
        ventana_juego.mostrar_ventana)

    # Logica inicio --> Ventana inicio
    logica_inicio.senal_validacion.connect(\
        ventana_inicio.recibir_validacion)

    ###

    ## Ranking --> **

    # Ventana Ranking --> Ventana inicio
    ventana_ranking.senal_volver_inicio.connect(\
        ventana_inicio.mostrar)
    # Logica Ranking --> Ventana Ranking
    logica_ranking.senal_enviar_jugadores.connect(\
        ventana_ranking.recibir_jugadores)

    ## Juego

    # Ventana juego --> Logica juego
    ventana_juego.senal_timer.connect(\
        logica_juego.iniciar_juego)
    ventana_juego.senal_parar_t_timer.connect(\
        logica_juego.detener_juego)
    ventana_juego.senal_tecla.connect(\
        logica_juego.revision_mov_froggy)
    ventana_juego.senal_verificar_colision.connect(\
        logica_juego.colision_objetos)
    ventana_juego.senal_reanudar_juego.connect(\
        logica_juego.reanudar_juego)
    ventana_juego.senal_froggy_tronco.connect(\
        logica_juego.colision_objetos)
    ## Movimiento AUTO
   
    
    # Logica juego --> Ventana juego
    logica_juego.senal_actualizar_tiempo.connect(\
        ventana_juego.set_time)
    logica_juego.senal_mov_froggy.connect(\
        ventana_juego.move_froggy)
    logica_juego.senal_colision_ver.connect(\
        ventana_juego.colision_verificada)
    logica_juego.senal_tocar_item.connect(\
        ventana_juego.item_tocado)
    logica_juego.senal_aparecer_objeto.connect(\
        ventana_juego.aparicion_items)
    logica_juego.senal_cerrar_ventana_juego.connect(\
        ventana_juego.salir)
    logica_juego.senal_actualizar_puntaje.connect(\
        ventana_juego.nivel_puntaje)
    # Auto
    logica_juego.thread_auto_1_l.senal_actualizar_auto.connect(\
        ventana_juego.mover_objeto)
    logica_juego.thread_auto_1_r.senal_actualizar_auto.connect(\
        ventana_juego.mover_objeto)
    logica_juego.thread_auto_2_l.senal_actualizar_auto.connect(\
        ventana_juego.mover_objeto)
    logica_juego.thread_auto_2_r.senal_actualizar_auto.connect(\
        ventana_juego.mover_objeto)
    logica_juego.thread_auto_3_l.senal_actualizar_auto.connect(\
        ventana_juego.mover_objeto)
    logica_juego.thread_auto_3_r.senal_actualizar_auto.connect(\
        ventana_juego.mover_objeto)
    logica_juego.thread_auto_4_l.senal_actualizar_auto.connect(\
        ventana_juego.mover_objeto)
    logica_juego.thread_auto_4_r.senal_actualizar_auto.connect(\
        ventana_juego.mover_objeto)
    logica_juego.thread_auto_5_l.senal_actualizar_auto.connect(\
        ventana_juego.mover_objeto)
    logica_juego.thread_auto_5_r.senal_actualizar_auto.connect(\
        ventana_juego.mover_objeto)
    logica_juego.thread_auto_6_l.senal_actualizar_auto.connect(\
        ventana_juego.mover_objeto)
    logica_juego.thread_auto_6_r.senal_actualizar_auto.connect(\
        ventana_juego.mover_objeto)
    # Tronco
    logica_juego.thread_tronco_1_l.senal_actualizar_auto.connect(\
        ventana_juego.mover_objeto)
    logica_juego.thread_tronco_1_r.senal_actualizar_auto.connect(\
        ventana_juego.mover_objeto)
    logica_juego.thread_tronco_2_l.senal_actualizar_auto.connect(\
        ventana_juego.mover_objeto)
    logica_juego.thread_tronco_2_r.senal_actualizar_auto.connect(\
        ventana_juego.mover_objeto)
    logica_juego.thread_tronco_3_l.senal_actualizar_auto.connect(\
        ventana_juego.mover_objeto)
    logica_juego.thread_tronco_3_r.senal_actualizar_auto.connect(\
        ventana_juego.mover_objeto)

        
    # Logica Juego --> Ventana post nivel
    logica_juego.senal_post_nivel_derrota.connect(\
        ventana_post_nivel.mostrar_ventana_derrota)
    logica_juego.senal_post_nivel_victoria.connect(\
        ventana_post_nivel.mostrar_ventana_victoria)

    ## Ventana post nivel --> Ventana juego
    ventana_post_nivel.senal_siguiente_nivel_ventana.connect(\
        ventana_juego.mostrar_ventana)
    ventana_post_nivel.senal_reordenar_labels.connect(\
        ventana_juego.set_geometrias)

    # Ventana post nivel --> logica juego

    ventana_post_nivel.senal_siguiente_nivel_ronda.connect(\
        logica_juego.pasar_nivel)
    ventana_post_nivel.senal_siguiente_nivel_threadl.connect(\
        logica_juego.thread_auto_1_l.pasar_nivel)
    ventana_post_nivel.senal_siguiente_nivel_threadl.connect(\
        logica_juego.thread_auto_2_l.pasar_nivel)
    ventana_post_nivel.senal_siguiente_nivel_threadl.connect(\
        logica_juego.thread_auto_3_l.pasar_nivel)
    ventana_post_nivel.senal_siguiente_nivel_threadl.connect(\
        logica_juego.thread_auto_4_l.pasar_nivel)
    ventana_post_nivel.senal_siguiente_nivel_threadl.connect(\
        logica_juego.thread_auto_5_l.pasar_nivel)
    ventana_post_nivel.senal_siguiente_nivel_threadl.connect(\
        logica_juego.thread_auto_6_l.pasar_nivel)
    ventana_post_nivel.senal_siguiente_nivel_threadr.connect(\
        logica_juego.thread_auto_1_r.pasar_nivel)
    ventana_post_nivel.senal_siguiente_nivel_threadr.connect(\
        logica_juego.thread_auto_2_r.pasar_nivel)
    ventana_post_nivel.senal_siguiente_nivel_threadr.connect(\
        logica_juego.thread_auto_3_r.pasar_nivel)
    ventana_post_nivel.senal_siguiente_nivel_threadr.connect(\
        logica_juego.thread_auto_4_r.pasar_nivel)
    ventana_post_nivel.senal_siguiente_nivel_threadr.connect(\
        logica_juego.thread_auto_5_r.pasar_nivel)
    ventana_post_nivel.senal_siguiente_nivel_threadr.connect(\
        logica_juego.thread_auto_6_r.pasar_nivel)
    ventana_post_nivel.senal_siguiente_nivel_threadl.connect(\
        logica_juego.thread_tronco_1_l.pasar_nivel)
    ventana_post_nivel.senal_siguiente_nivel_threadl.connect(\
        logica_juego.thread_tronco_2_l.pasar_nivel)
    ventana_post_nivel.senal_siguiente_nivel_threadl.connect(\
        logica_juego.thread_tronco_3_l.pasar_nivel)
    ventana_post_nivel.senal_siguiente_nivel_threadr.connect(\
        logica_juego.thread_tronco_1_r.pasar_nivel)
    ventana_post_nivel.senal_siguiente_nivel_threadr.connect(\
        logica_juego.thread_tronco_2_r.pasar_nivel)
    ventana_post_nivel.senal_siguiente_nivel_threadr.connect(\
        logica_juego.thread_tronco_3_r.pasar_nivel)


    ## Ventana post nivel --> logica post nivel
    ventana_post_nivel.senal_guardar_puntajes.connect(\
        logica_post_nivel.guardar_jugadores)


    ventana_inicio.mostrar()
    app.exec()