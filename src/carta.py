from src.boton import Boton
import pygame

class Carta(Boton):
    """Clase Carta: Guarda la informacion de cada carta y hereda de la clase Boton.
        
        Inicializa los atributos: 
        - _valor el cual es el numero de la carta 
        - _palo es la figura de la carta
        - x_final sirven para las animaciones
        - y_final sirven para las animaciones
        - velodidad sirve para la velocidad de las animaciones
        - seleccionada devuelve si esta seleccionada la carta.
        
    """
    PALOS = ["o", "c", "e", "b"]    # Oros(o), Copas(c), Espadas(e), Bastos(b)
    VALORES = list(range(1,13))

    _cache_filtros = {}
    @classmethod
    def _get_cache_filtro(cls, valor, palo):
        carta = (valor, palo)
        if carta not in cls._cache_filtros:
            imagen = pygame.image.load(f"Graficos/cartas/{valor}{palo}.png").convert_alpha()
            filtro = pygame.Surface(imagen.get_size(), pygame.SRCALPHA)
            filtro.fill((0, 0, 60, 180))
            imagen.blit(filtro, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            cls._cache_filtros[carta] = imagen
        return cls._cache_filtros[carta]

    def __init__(self, valor, palo):
        super().__init__(f"Graficos/cartas/{valor}{palo}.png", 1200, 600, "Sonidos/sonido_seleccionar_cartas.mp3")
        self._valor = valor
        self._palo = palo
        self.x_final = self.x
        self.y_final = self.y
        self.velocidad = 0.2
        self.seleccionada = False
        self.habilitada = True

    @property
    def valor(self):
        if self.habilitada:
            return self._valor
        else:
            return 0

    @property
    def palo(self):
        return self._palo
    
    def mover_hacia_destino(self):
        """Funcion mover_hacia_destino: cambia la posicion actual de la carta hasta 
            llegar a la posicion final, para la animacion."""
        x = self.x
        y = self.y
        x += (self.x_final - self.x) * self.velocidad
        y += (self.y_final - self.y) * self.velocidad
        super().asignar_posicion(x, y)

    def dibujar(self, screen):
        """Funcion dibujar: accede a la funcion mover_hacia_destino y muestra la carta."""
        self.mover_hacia_destino()
        super().dibujar(screen)
        if not self.habilitada:
            imagen = Carta._get_cache_filtro(self._valor, self._palo)
            screen.blit(imagen, (self.x, self.y))

    def detectar_seleccion(self, eventos):
        """Funcion deterctar_seleccion: detecta si se le ha dado click a la carta y 
            devuelve true o false"""
            
        if self.detectar_click(eventos):
            self.seleccionada = not self.seleccionada
            if self.seleccionada:
                return True
            else:
                return False