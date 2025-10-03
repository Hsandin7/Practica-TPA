# Naipo

![Menu Principal](Graficos\Menu_principal.jpg)

##

### Como usar:
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

    class Carta {
	    +String nombre
	    +void Funcionamiento()
    }
    class Comodin {
	    +String nombre
	    +String tipo
	    +int precio
	    +void Funcionamiento()
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
    class CartaNormal {
	    +int numero
	    +String color
	    +void Funcionamiento()
    }
    Carta --|> Comodin
    Carta --|> CartaNormal
    Comodin --|> ComodinNormal
    Comodin --|> ComodinRaro
    Comodin --|> ComodinEpico
    class Niveles{
        +int puntuación 
        +String NombreNivel
        +void Recompensas()
    }
    class Nivel1{
        +int puntuación 
        +String NombreNivel = nivel1
        +void Recompensas()
    }
    class Nivel2{
        +int puntuación 
        +String NombreNivel = nivel2
        +void Recompensas()
    }
    Niveles --|> Nivel1
    Niveles --|> Nivel2
```