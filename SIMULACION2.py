# -*- coding: utf-8 -*-
import time
import pygame
from pygame.locals import *
import os
import sys
import random
# -----------
# Constantes

SCREEN_WIDTH = 1336
SCREEN_HEIGHT = 768


# Clases y Funciones utilizadas
def gale():
    x = int(time.strftime("%H%M%S%S"))
    #print(x)
    ale=0.0
    r = ([0,0,0,0,0,0,0,0])
    factor =([10000000,1000000,100000,10000,1000,100,10,1])

    for i in range(1):
        #print (x);
        n=x*x;
    
        #print (n);
        r[0] = int(n/10000000);
        
        n=n-(r[0]*factor[0]);
        #print (n)
        r[1] = int(n/1000000);  
        n=n-(r[1]*factor[1]);   
        r[2] = int(n/100000);
        n=n-(r[2]*factor[2]);
        r[3] =int( n/10000);
        n=n-(r[3]*factor[3]);
        r[4] =int(n/1000);
        n=n-(r[4]*factor[4]);
        r[5] = int(n/100);
        n=n-(r[5]*factor[5]);
        r[6] = int(n/10);
        n=n-(r[6]*factor[6]);
        r[7] = int(n/1);
        #print(r);
        ni=2
        for j in range(2,6):
            ale=ale+(r[j]*factor[j])
            #print("factorp: ",r[j]*factor[j]); 
        ale=ale/factor[5]
        #print("numero aleatorio:",ale)
        x=ale
        n=0;
        ale=0;
        #print("dato ",i+1)
        #print (x%100)
    return x

# Creamos los sprites (clases) de los objetos del juego:

class Pelota(pygame.sprite.Sprite):
    #La bola y su comportamiento en la pantalla"
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bola.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.centery = SCREEN_HEIGHT / 2
        self.speed = [3, 3]
#actualizamos la posision de la pelota con respecto a un movimiento pred
    def update(self):
        if self.rect.left<0 or self.rect.right > SCREEN_WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed[1] = -self.speed[1]
        self.rect.move_ip((self.speed[0], self.speed[1]))
        #determinamos si la pelota choca con algo
    def colision(self, objetivo):
        if self.rect.colliderect(objetivo.rect):
            self.speed[0] = -self.speed[0]
            #carga el sonido
            sonido1=pygame.mixer.Sound("Click1.ogg")
            #reproduce el sonido
            sonido1.play()

class Paleta(pygame.sprite.Sprite):
    "Define el comportamiento de las paletas de ambos jugadores"

    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("paleta.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = SCREEN_HEIGHT / 2

    def humano(self):
        # Controlar que la paleta no salga de la pantalla
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        elif self.rect.top <= 0:
            self.rect.top = 0

    def cpu(self,objetivo):
        #self.speed = [0, 2.5]
        #if Pelota.speed[0] >= 0 and Pelota.rect.centerx >= SCREEN_WIDTH / 2:
          #  if self.rect.centery > Pelota.rect.centery:
            #    self.rect.centery -= self.speed[1]
            #if self.rect.centery < Pelota.rect.centery:
              #  self.rect.centery += self.speed[1]

#algoritmo que hace invencible al oponente {
        self.rect.centery=objetivo.rect.centery
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        elif self.rect.top <= 0:
            self.rect.top = 0


# ------------------------------
# Funcion principal del juego


def main():
    pygame.init() #inicializacion de todos los modulos
    pantalla=pygame.display.set_mode([1366,768])
    #determina el tamaño de ventana y crea una supeficie
    pygame.display.set_caption("SIMULACION")#titulo de la ventana

    fondo = pygame.image.load("mapa.jpg").convert()

    salir= False
    reloj1=pygame.time.Clock() #iniciamos reloj
    blanco=(225,225,225) #determinando un color con escala rgb
    rojo=(200,20,50)
    azul=(70,70,190)

#trozo de codigo para crear texto
#se determina la fuente y el tamaño
    fuente1=pygame.font.Font(None, 30)
    fuente2=pygame.font.Font(None,25)
    #se cre la superficie del texto con los parametros de :
    #la fuente a mostrar,texto a escribir y color del texto
    texto1=fuente1.render("Simulacion del movimiento de un auto en una carretera",0,(0,0,0))
    texto2=fuente2.render("variables aleatorias discretas",0,(0,0,0))
    texto3=fuente2.render("numero de baches:",0,(0,0,0))
    texto4=fuente2.render("numero de personas en el auto:",0,(0,0,0))
    texto5=fuente2.render("variables aleatorias continuas",0,(0,0,0))
    texto6=fuente2.render("velocidad del viento:",0,(0,0,0))
    texto6m=fuente2.render("km/h",0,(0,0,0))
    texto7=fuente2.render("angulo del viento:",0,(0,0,0))
    texto7m=fuente2.render("grados",0,(0,0,0))
    texto8=fuente2.render("cantidad de gasolina:",0,(0,0,0))
    texto8m=fuente2.render("litros",0,(0,0,0))
    texto9=fuente2.render("velocidad del auto:",0,(0,0,0))
    x1=str(gale()%10)
    x2=str((gale()%10)+1)
    x3=str((gale()%100)+((gale()/100)))
    x4=str((gale()%1)+((gale()/100)))
    x5=str((gale()/1000)+(gale()/1000))
    x6=str((gale()%100)+((gale()/100))+((gale()/100)))


    texto1r=fuente2.render(x1,0,(0,0,0))
    texto2r=fuente2.render(x2,0,(0,0,0))
    texto3r=fuente2.render(x3,0,(0,0,0))
    texto4r=fuente2.render(x4,0,(0,0,0))
    texto5r=fuente2.render(x5,0,(0,0,0))
    texto6r=fuente2.render(x6,0,(0,0,0))


    superficie1=pygame.Surface((100,150))#crea nueva superficie con dimencion 100*150
    superficie1.fill(rojo) #se pinta la nueva superficie de rojo


    while salir!=True:#loop principal
        for event in pygame.event.get(): #checa todos los eventos
            if event.type ==pygame.QUIT: #checa si se presiona x
                salir=True

        reloj1.tick(20) #reloj que actualiza la pantallla cada 20 frames
        pantalla.fill(blanco) # pinta la pantalla de color blanco
#muestra la superficie1 en coordenada 50,70
      
        #DIBUJA EN LA SUPERFICIE DE PANTALLA EL TEXTO
        #EN LA COORDENADA 100,200

        pantalla.blit(fondo, (0,0))
        pantalla.blit(texto1,(10,10))
        pantalla.blit(texto2,(10,35))
        pantalla.blit(texto3,(10,55))
        pantalla.blit(texto4,(10,75))
        pantalla.blit(texto5,(10,110))

        pantalla.blit(texto6,(10,130))
        pantalla.blit(texto6m,(280,130))
        pantalla.blit(texto7,(10,152))
        pantalla.blit(texto7m,(280,152))
        pantalla.blit(texto8,(10,173))
        pantalla.blit(texto8m,(280,173))
        pantalla.blit(texto9,(10,195))

        pantalla.blit(texto1r,(300,55))
        pantalla.blit(texto2r,(300,75))
        pantalla.blit(texto3r,(200,130))
        pantalla.blit(texto4r,(200,152))
        pantalla.blit(texto5r,(200,173))
        pantalla.blit(texto6r,(200,195))
        pantalla.blit(texto6m,(280,195))

        

        pygame.display.update() #refresca la pantalla

    pygame.quit() #cierrra la ventana al presionar el boton x

if __name__ == "__main__":

    main()


