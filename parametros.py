import os


# Mapa
MAX_X = 750
MIN_X = 0
MIN_Y = 150
MAX_Y = 650


## Teclas
TECLA_ARRIBA = "w"
TECLA_IZQUIERDA = "a"
TECLA_ABAJO = "s"
TECLA_DERECHA = "d"
SALTO_DISCRETO = " "
TECLA_PAUSA = "p"

## Personaje
VIDAS_INICIO = 5
VELOCIDAD_CAMINAR = 20 ## Velocidad de movimiento Froggy
PIXELES_SALTO = None ## Pixeles que se mueve Froggy al saltar

## Juego
TIEMPO_AUTOS = 0.2 ## Tiempo cada el cual aparecen autos en pantalla
VELOCIDAD_AUTOS = 2 ## Velocidad a la que se mueven los autos
TIEMPO_TRONCOS = 0.2 ## Tiempo cada el cual aparecen troncos en pantalla
VELOCIDAD_TRONCOS = 2 ##Velocidad a la que se mueven los troncos
TIEMPO_AVANCE = 0.012
# Froggy
POS_X_FROGGY = 370
POS_Y_FROGGY = 650
# Auto 1 (Rojo)
# Va hacia la izquierda
POS_X_AUTO_1_L = 800
POS_Y_AUTO_1_L = 570
# Va hacia la derecha
POS_X_AUTO_1_R = -60
POS_Y_AUTO_1_R = 570

# Auto 2 (Plata)
# Va hacia la izquierda
POS_X_AUTO_2_L = 800
POS_Y_AUTO_2_L = 540
# Va hacia la derecha
POS_X_AUTO_2_R = -60
POS_Y_AUTO_2_R = 540

# Auto 3 (Blanco)
# Va hacia la izquierda
POS_X_AUTO_3_L = 800
POS_Y_AUTO_3_L = 500
# Va hacia la derecha
POS_X_AUTO_3_R = -60
POS_Y_AUTO_3_R = 500

# Auto 4 (Negro)
# Va hacia la izquierda
POS_X_AUTO_4_L = 800
POS_Y_AUTO_4_L = 265
# Va hacia la derecha
POS_X_AUTO_4_R = -60
POS_Y_AUTO_4_R = 265

# Auto 5 (Morado)
# Va hacia la izquierda
POS_X_AUTO_5_L = 800
POS_Y_AUTO_5_L = 230
# Va hacia la derecha
POS_X_AUTO_5_R = -60
POS_Y_AUTO_5_R = 230

# Auto 6 (Azul)
# Va hacia la izquierda
POS_X_AUTO_6_L = 800
POS_Y_AUTO_6_L = 200
# Va hacia la derecha
POS_X_AUTO_6_R = -60
POS_Y_AUTO_6_R = 200

##### TRONCOS
# TRONCO 1 (Desde arriba hacia abajo)
# Va hacia la izquierda
POS_X_TRONCO_1_L = 800
POS_Y_TRONCO_1_L = 415
# Va hacia la derecha
POS_X_TRONCO_1_R = -60
POS_Y_TRONCO_1_R = 415

# Tronco 2
# Va hacia la izquierda
POS_X_TRONCO_2_L = 800
POS_Y_TRONCO_2_L = 385
# Va hacia la derecha
POS_X_TRONCO_2_R = -60
POS_Y_TRONCO_2_R = 385

# Tronco 3
# Va hacia la izquierda
POS_X_TRONCO_3_L = 800
POS_Y_TRONCO_3_L = 360
# Va hacia la derecha
POS_X_TRONCO_3_R = -60
POS_Y_TRONCO_3_R = 360

## Objetos
TIEMPO_OBJETO = 15 ## Tiempo cada el cual aparece uno de los objetos especiales
    ##Este objeto sera elegido de manera aleatoria cada ese intervalo de tiempo
CANTIDAD_MONEDAS = 25 ## CAntidad de monedas que se le suman al jugador
##Despues de agarrar uno de los objetos especiales

## Dificultad juego
DURACION_RONDA_INICIAL = 120
PONDERADOR_DIFICULTAD = 0.95 ## Numero que hace cambiar la velocidad de autos y troncos
## Tambien hace cambiar la duracion de la ronda

## Ventana de inicio
MIN_CARACTERES = 2 ## Cantidad minima de caracteres nombre de usuarios
MAX_CARACTERES = 10 ## Cantidad maxima de caracteres nombre de usuarios
TAMAÑO_VENTANA = (200, 200, 300, 400)

## Trampa
VIDAS_TRAMPA = None

## Rutas
RUTA_LOGO = os.path.join("sprites", "Logo.png")
RUTA_ICONO = os.path.join("frontend", "assets", "rana.png")
RUTA_UI_VENTANA_JUEGO = os.path.join("frontend", "assets", "ventana_juego.ui")
RUTA_UI_VENTANA_POST_NIVEL = os.path.join("frontend", "assets", "post_nivel.ui")
RUTA_PASTO = os.path.join("sprites", "Mapa", "areas", "pasto.png")
RUTA_FROGGY_TRISTE = os.path.join("frontend", "assets", "froggy_triste.png")
RUTA_FROGGY_PAUSE = os.path.join("frontend", "assets", "froggy_pause.png")

## Ruta Juego
# Froggy
RUTA_FROGGY_STILL = os.path.join("sprites", "Personajes", "Verde", "still.png")
RUTA_FROGGY_UP = os.path.join("sprites", "Personajes", "Verde", "up_1.png")
RUTA_FROGGY_DOWN = os.path.join("sprites", "Personajes", "Verde", "down_1.png")
RUTA_FROGGY_RIGHT = os.path.join("sprites", "Personajes", "Verde", "right_1.png")
RUTA_FROGGY_LEFT = os.path.join("sprites", "Personajes", "Verde", "left_1.png")
# Auto
RUTA_AUTO_ROJO_L = os.path.join("sprites", "Mapa", "autos", "rojo_left.png")
RUTA_AUTO_ROJO_R = os.path.join("sprites", "Mapa", "autos", "rojo_right.png")
RUTA_AUTO_PLATA_L = os.path.join("sprites", "Mapa", "autos", "plata_left.png")
RUTA_AUTO_PLATA_R = os.path.join("sprites", "Mapa", "autos", "plata_right.png")
RUTA_AUTO_BLANCO_L = os.path.join("sprites", "Mapa", "autos", "blanco_left.png")
RUTA_AUTO_BLANCO_R = os.path.join("sprites", "Mapa", "autos", "blanco_right.png")
RUTA_AUTO_NEGRO_L = os.path.join("sprites", "Mapa", "autos", "negro_left.png")
RUTA_AUTO_NEGRO_R = os.path.join("sprites", "Mapa", "autos", "negro_right.png")
RUTA_AUTO_MORADO_L = os.path.join("sprites", "Mapa", "autos", "morado_left.png")
RUTA_AUTO_MORADO_R = os.path.join("sprites", "Mapa", "autos", "morado_right.png")
RUTA_AUTO_AZUL_L = os.path.join("sprites", "Mapa", "autos", "azul_left.png")
RUTA_AUTO_AZUL_R = os.path.join("sprites", "Mapa", "autos", "azul_right.png")

# Carretera
RUTA_CARRETERA = os.path.join("sprites", "Mapa", "areas", "carretera.png")
# Rio
RUTA_RIO = os.path.join("sprites", "Mapa", "areas", "rio.png")
# Tronco
RUTA_TRONCO = os.path.join("sprites", "Mapa", "elementos", "tronco.png")

## Items
RUTA_CALAVERA = os.path.join("sprites", "Objetos", "Calavera.png")
RUTA_CORAZON = os.path.join("sprites", "Objetos", "Corazon.png")
RUTA_MONEDA = os.path.join("sprites", "Objetos", "Moneda.png")
RUTA_RELOJ = os.path.join("sprites", "Objetos", "Reloj.png")