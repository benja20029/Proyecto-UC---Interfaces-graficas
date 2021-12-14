# DCCrossy Frog :school_satchel:


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:


<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>
<El codigo no posee implementacion completa de cambio de sprites en froggy, 
no se realiza el salto discreto, las colisiones con los troncos hacen que Froggy los siga
hasta que los troncos desaparecen del mapa y los cheatcodes no fueron implementados.
 Mas alla de eso, el juego funciona perfectamente. Hay algo que no se pudo solucionar y es que la tecla
 P logre reanudar el juego, la tecla P logra pausar el juego, sin embargo, para reanudarlo, 
 esto se debe hacer mediante la tecla escape. Por ultimo, debido a que no se explicito, se supone
 que al salir del juego desde la ventana de juego, no se guardaran los puntajes.
 Luego, se comenta que se dejo comentada la linea 283 
 (verificacion de colision con rio), debido a que dificultaria la revision del juego, 
 pues, no se pudo implementar de manera correcta el movimiento de Froggy con los troncos.
  Sin embargo, la colision con el rio es detectada y Froggy pierde una vida si choca con el, 
  solo no quise dificultar la revision. >
### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Ventana de Inicio: 4 pts (3%)
##### ✅ Ventana de Inicio <Fue implementada correctamente>
#### Ventana de Ranking: 5 pts (4%)
##### ✅ Ventana de Ranking <Fue implementada correctamente\>
#### Ventana de juego: 13 pts (11%)
##### ✅ Ventana de juego <Fue implementada correctamente\>
#### Ventana de post-nivel: 5 pts (4%)
##### ✅ Ventana post-nivel <Fue implementada correctamente\>
#### Mecánicas de juego: 69 pts (58%)
##### 🟠 Personaje <Froggy no posee salto discreto y no tiene mas de un sprite para cada lado\>
##### 🟠 Mapa y Áreas de juego <Si se pisan los troncos hacen que froggy los siga hasta salir del mapa\>
##### ✅ Objetos <Se implementan correctamente\>
##### ✅ Fin de Nivel <Se implementa correctamente\>
##### ✅ Fin del juego <Se implementa correctamente\>
#### Cheatcodes: 8 pts (7%)
##### ✅ Pausa <Funciona bien, a excepcion de la problematica que se especifico mas arriba\>
##### ❌ V + I + D <No se implemento\>
##### ❌ N + I + V <No se implemento\>
#### General: 14 pts (12%)
##### ✅ Modularización <Se definen backend para logica y frontend para diseño\>
##### ✅ Modelación <Se respeta pep-8\>
##### ✅ Archivos  <Se utilizan correctamente los archivos y se escriben de manera correcta los puntajes\>
##### ✅ Parametros.py <Se implementan todos los parametros, los que no se usaron se dejaron como NoneType\>
#### Bonus: 10 décimas máximo
##### ❌ Ventana de Tienda <No se implemento\>
##### ❌ Música <No se implemento\>
##### ❌ Checkpoint <no se implemento\>
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```parametros.py``` en ```T2```
2. ```puntajes.txt``` en ```T2```
3. ```sprites``` en ```T2```
4. ```logica_inicio.py``` en ```T2/backend```
5. ```logica_ranking.py``` en ```T2/backend```
6. ```logica_juego.py``` en ```T2/backend```
7. ```logica_post_nivel.py``` en ```T2/backend```
8. ```ventana_inicio.py``` en ```T2/frontend```
9. ```ventana_ranking.py``` en ```T2/frontend```
10. ```ventana_juego.py``` en ```T2/frontend```
11. ```ventana_post_nivel.py``` en ```T2/frontend```
12. ```froggy_pause.png``` en ```T2/frontend/assets```
13. ```post_nivel.ui``` en ```T2/frontend/assets```
14. ```ventana_juego.ui``` en ```T2/frontend/assets```
15. ```rana.png``` en ```T2/frontend/assets```

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```Pyqt5.QtCore```: ```pyqtSignal```, ```QRect```, ```QThread```, ```QTimer```
2. ```PyQt5.QtWidgets```: ```Qlabel```, ```QMessageBox```,```QHBoxLayout```,```QVBoxLayout```\
,```QPushButton```,```QWidget```,```QLineEdit```(debe instalarse)
1. ```Pyqt5.QtGui```: ```QIcon```, ```QPixMap```,```QFont```
1. ```Pyqt5```: ```uic```
1. ```os```: ```path.join```
1. ```time```: ```sleep```, ```QRect```
1. ```random```: ```choice```, ```QRect```
3. ...

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```logica_inicio.py```: Contiene a ```LogicaInicio```
2. ```logica_juego.py```: Contiene a ```ThreadL```, ```ThreadR```, ```LogicaJuego``` 
(Los threads se podrian combinar en uno pero por temas de tiempo, no se alcanzo)
3. ```logica_post_nivel.py```: Contiene a ```LogicaPostNivel```
4. ```logica_ranking.py```: Contiene a ```LogicaRanking```
5. ```ventana_inicio.py```: Contiene a ```VentanaInicio```
6. ```ventana_juego.py```: Contiene a ```VentanaJuego```
7. ```ventana_post_nivel.py```: Contiene a ```VentanaPostNivel```
8. ```ventana_ranking.py```: Contiene a ```VentanaRanking```
9. ```parametros.py```: Contiene todos los valores fijos que se usaran en el juego
3. ...

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Se supone que al salir del juego desde la ventana de juego no es necesario 
guardar los puntajes del usuario hasta ese momento, debido a que no salia en el enunciado.> 
2. <Para reanudar el juego una vez se lleve a pausa, esto se puede hacer mediante
 el boton escape, lo que reanudara todo de manera normal>
3. <Descomentar linea 283 si se quiere verificar la correcta deteccion de colision
 de Froggy con el rio, esta linea fue comentada para facilitar la revision, pues, hubieron 
 problemas en los movimientos con el tronco y Froggy>

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


-------



**EXTRA:** si van a explicar qué hace específicamente un método, no lo coloquen en el README mismo. Pueden hacerlo directamente comentando el método en su archivo. Por ejemplo:

```python
class Corrector:

    def __init__(self):
          pass

    # Este método coloca un 6 en las tareas que recibe
    def corregir(self, tarea):
        tarea.nota  = 6
        return tarea
```

Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

```python
def funcion(argumento):
    """
    Mi función hace X con el argumento
    """
    return argumento_modificado
```
Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<link de código>: este hace \<lo que hace> y está implementado en el archivo <nombre.py> en las líneas <número de líneas> y hace <explicación breve de que hace>



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
