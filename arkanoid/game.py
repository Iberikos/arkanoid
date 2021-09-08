import pygame as pg
from arkanoid import ALTO, ANCHO
#from . import ALTO, ANCHO ---> se pueden de las 2 formas
from arkanoid.escenas import Portada, Partida, Record


pg.init()

class Game():
    def __init__(self):
        pantalla = pg.display.set_mode((ANCHO, ALTO))
        self.escenas = [Portada(pantalla), Partida(pantalla)]
        
    def launch(self):
        i = 0
        while True:
            self.escenas[i].bucle_principal()
            i += 1
            if i == len(self.escenas):
                i = 0    
            # fórmula equivalente al if de arriba
            # i = (i + 1) % len(self.escenas)