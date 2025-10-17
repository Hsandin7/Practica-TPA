# Naipo

![Pagina Principal](Graficos/pagina_principal.png)

##

### Como usar:
Ejecutar desde el main.py

Este juego utiliza la versión 3.13 de python junto con la biblioteca pygame 2.6.1

Esta se puede instalar desde "requirements.txt" de la siguiente forma:

```
pip install -r requirements.txt
```

##

### Diagrama de clases:

```mermaid
classDiagram
direction TB

    class boton {
	    + int posx
	    + int posy
	    + imagen
	    + sonido
	    + imagen oscurecida
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
	    +dibujar()
	    +Funcionamiento()
    }
    class ComodinNormal {
	    +String nombre
	    +String tipo = normal
	    +int precio
	    +void Funcionamiento()
    }
    class ComodinRaro {
	    +String nombre
	    +String tipo = raro
	    +int precio
	    +void Funcionamiento()
    }
    class ComodinEpico {
	    +String nombre
	    +String tipo = epico
	    +int precio
	    +void Funcionamiento()
    }
    boton --|> Carta
    boton--|> Comodin
    Comodin --|> ComodinNormal
    Comodin --|> ComodinRaro
    Comodin --|> ComodinEpico
    
    class evaluador_cartas{
	    + lista cartas_seleccionadas
	    + diccionario resultado
	    + evaluar()
	    + comprobaciones()
	  }
	  
	  class Mazo{
		  + lista baraja
		  + barajar()
		  + robar()
	  }
	  
	  class jugador{
		  + puntos
		  + puntos_cartas
		  + multiplicador
		  + mazo
		  + mano
		  + cartas_jugadas
		  + limite_seleccion
		  + mostrar_puntos()
		  + mostrar_mano()
		  + detectar_seleccion_carta()
		  + jugar_cartas()
		  + descartar_cartas()
	  }
	  
	  class transicion{
	  }
```
