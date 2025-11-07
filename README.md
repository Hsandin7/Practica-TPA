# Naipo

![Pagina Principal](Graficos/pagina_principal.png)

##

1. [Requisitos](#Requisitos)
2. [Clonar este repositorio](#ClonarRepo)
3. [Entorno Virtual](#Venv)
    * 3.1 [Crear Entorno Virtual](#CrearVenv)
    * 3.2 [Inicializar Entorno Virtual](#InicializarVenv)
    * 3.3 [Instalar dependencias](#Dependencias)
    * 3.4 [Comprobación](#Comprobacion)
4. [Ejecución](#Ejecucion)
5. [Diagrama de clases](#Diagrama)

##  1. <a name='Requisitos'>Requisitos</a>

Es necesario tener instalado python 3.13 o posterior.

Este repositorio usa concretamente la versión 3.13.7 de python:  [python.org/downloads/release/python-3137](https://www.python.org/downloads/release/python-3137/)


##  2. <a name='ClonarRepo'>Clonar este repositorio</a>

Para clonar el repositorio se necesita ejecutar:

```
git clone https://github.com/Hsandin7/Practica-TPA.git [subcarpeta]
```

donde `[subcarpeta]` es opcional, si se especifica designa el path relativo de una subcarpeta donde quedará alojado el repositorio.


##  3. <a name='Venv'>Entorno Virtual</a>

###  3.1 <a name='CrearVenv'>Crear Entorno Virtual</a>

Para crear el entorno virtual se debe introducir en la terminal:

```
python -m venv .venv
```

Seleccionando el compilador de python correspondiente (python 3.13.x)

###  3.2 <a name='InicializarVenv'>Inicializar Entorno Virtual</a>

Según el sistema operativo, se inicializará el entorno virtual introduciendo en la terminal:

```
# Windows:
.venv\Scripts\activate
```
```
# Linus o MacOS:
source .venv/bin/activate
```

###  3.3 <a name='Dependencias'>Instalar dependencias</a>

Finalmente, se instalan las dependencias introduciendo en la terminal:

```
pip install -r requirements.txt
```

###  3.4 <a name='Comprobacion'>Comprobación</a>

Para comprobar que se ha creado e inicializado correctamente se puede introducir en la terminal:

```
pip list
```

Si se ha creado todo correctamente debería devolver algo así:

```
Package Version
------- -------
pip     25.2
pygame  2.6.1
```

##  4. <a name='Ejecucion'>Ejecución</a>

Para iniciar el proyecto hay que ejecutar el main.py

Para ello, se puede ejecutar desde el editor de código que esté usando o introduciendo en la terminal:

```
python main.py
```


##  5. <a name='Diagrama'>Diagrama de clases</a>

```mermaid
classDiagram
direction TB
    class Juego {
        +int pagina_actual
        +list paginas
        +dict botones
        +bool mostrar_fondo
        +Jugador jugador
        +Tienda tienda
        +cargar_paginas()
        +cargar_botones()
        +reiniciar()
        +mostrar_pagina_principal()
        +actualizar_pagina_principal()
        +mostrar_pagina_juego()
        +actualizar_pagina_juego()
        +mostrar_menu_salida()
        +actualizar_menu_salida()
        +mostrar_menu_tienda()
        +actualizar_menu_tienda()
        +mostrar_menu_guardado()
        +actualizar_menu_guardado()
        +mostrar_pagina_game_over()
        +actualizar_pagina_game_over()
        +mostrar_pantalla_info()
    }
    class Boton {
	    + int posx
	    + int posy
	    + imagen
	    + sonido
		+ caché imagenes
		+ caché hover
	    + asignarPosicion()
	    + Dibujar()
	    + detectar_click()
    }
    class Carta {
	    +int valor 
	    +string palo
	    +int posicion_final_x
	    +int posicion_final_y
	    +float velocidad
	    +bool seleccionada
	    +mover_hacia_destino()
	    +dibujar()
	    +detectar_seleccion()
    }
    class Comodin {
	    +String descripcion
	    +String nombre
	    +int raraza
	    +int precio
		+bool seleccionada
		+bool arrastrada
	    +dibujar()
	    +aplicar()
		+mover_comodines()
		+dibujar()
    }
    class Evaluador_Cartas{
	    + list cartas
	    + dict resultado
	    + evaluar()
	    + comprobaciones()
		+_escalera_color()
		+_poker()
		+_trio_y_pareja()
		+_color()
		+_escalera()
		+_trio()
		+_doble_pareja()
		+_pareja()
		+_carta_mas_alta()
	}
	class Mazo{
		+ list cartas
		+ barajar()
		+ robar()
	}
	class Jugador{
		+ int puntos
		+ int puntos_cartas
		+ int puntos_nivel
		+ int multiplicador
		+ bool nivel_completado
		+ bool game_over
		+ int numero_nivel
		+ int dinero
		+ list mano
		+ lisr comodines_mano
		+ cartas_jugadas
		+ cartas_descartadas
		+ cartas_seleccionadas
		+ int limite_seleccion
		+ int limite_descartes
		+ limite_seleccion
		+ mostrar_puntos()
		+ mostrar_mano()
		+ mostrar_cartas()
		+ actualizar()
		+ detectar_seleccion_carta()
		+ jugar_cartas()
		+ descartar_cartas()
		+ guardar_partida()
		+ cargar_partida()
		+ borrar_partida()
		+ siguiente_ronda()
    }
    class Guardado{
		+ string archivo_guardado
		+ inicializar_archivo_guardado()
		+ guardar_partida()
		+ cargar_partida()
		+ borrar_partdia()
		+ mostrar_info_slots()
	}
	class Niveles{
		+ int nivel_actual
		+ int puntos_nivel
		+ int multiplicador
		+ tuple color_pantalla
	 	+ list colores_boss
		+ bool es_boss
		+ int carta_invalida
		+ siguiente_nivel()
		+ check_boss()
		+ dibujar_filtro_pantalla()
	}
    class Tienda{
        + jugador
        + list comodines_disponibles
        + int coste_cambiar
        + list tienda_comodines
        + comodin_seleccionado
        + imagen_descripcion
        + poblar()
        + mostrar()
        + actualizar()
        + cambiar()
        + comprar()
    }
    class Transicion{
        + int valor
        + string fase
        + list paginas
        + int num_pagina_destino
        + int angulo
        + int animacion
        + iniciar()
        + actualizar()
        + animacion_inicio()
        + animacion_tienda()
        + animacion_gameover()
    }
    class Texto{
        + cargar_fuente()
        + mostrar_texto()
        + mostrar_texto_centrado()
        + mostrar_texto_transparente()
        + mostrar_texto_multilinea()
    }

    %% Herencias
    Boton <|-- Carta
    Boton <|-- Comodin

    %% Asociaciones / composiciones (direccionales)
    Juego o-- Jugador : jugador
    Juego o-- Tienda : tienda
    Juego "1" o-- "many" Boton : botones

    Jugador o-- Mazo : mazo
    Jugador o-- Evaluador_Cartas : evaluador
    Jugador o-- Animador_Texto : animador_texto
    Jugador o-- Niveles : niveles
    Jugador o-- Guardado : guardado
    Jugador "8" o-- "0..8" Carta : mano
    Jugador "0..5" o-- "0..5" Comodin : comodines_mano

    Tienda o-- Comodin : tienda_comodines "2"

    Comodin ..> Evaluador_Cartas : usa efectos (funciones registradas)
    Carta ..> Boton : hereda comportamiento (imagen/rect/sonido)

    Transicion ..> Juego : pagina destino (uso en runtime)

    Texto <.. Animador_Texto : usa métodos estáticos    
```
