# -*- coding: utf-8 -*-

#-------------------------------------------------------------
#acevedo maldonado josue (neomatrix)
#vasquez martinez agustin (maldad)
#---------------------------------------------------------------

import time
import pygame
from pygame.locals import *
import os
import sys
import random
import math
# -----------
# Constantes

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 760
mensajem="_"
#parametros del auto
puntoinicialautox=100
puntoinicialautoy=300
velocidadautox=0
velocidadautoy=0


gasolinatotal=0

posis = [1386,1000,1200,900,1300,800,1500,1400,1700,1100]
possx = [0,-300,-600,-900,-1200,-1400,150,-750,210,1100]
imagenes=["autoblanco2.png","autoamarillo.png","automorado.png"]
izquierda=-30
derecha=30


# Clases y Funciones utilizadas
def rotar_coche(self, angle):
      self.image = pygame.transform.rotate(self.image, angle)

def girar_coche(self,g):
	self.action=g
   	self.area = pygame.rect.Rect(self.actions[self.action])
        


def funcionmov(x,c):
    #y = (-0.00100045*(x**2))+(1.50355859*(x))-(3.09970763)
    if(c==1):
        #1 curva
        y = (-1.37329904E-24*(x**10))+(8.80761563E-21*(x**9))-(2.38715527E-17*(x**8))+(3.55533353E-14*(x**7))-(3.16989232E-11*(x**6))+(1.73077673E-08*(x**5))-(5.70586401E-06*(x**4))+(0.00108526*(x**3))-(0.10923901*(x**2))+(4.85010885*x)+347.99999328
    if(c==2):
        #2 curvas
        y = (2.38222222E-06*(x**3))-(0.00465244*(x**2))+(2.02222222*x)+348
    if(c==3):
        #3curvas
        y = (-7.72683034E-09*(x**4))+(2.05437944E-05*(x**3))-(0.01640877*(x**2))+(3.70515822*x)+348
    return y

def genera_continuadistancia():
	# promedio del camino = 100 km
	prom = 100
	q=2.9
	v1 = random.random()
	v2 = random.random()
	#r= ((v1)**2)+((random.random())**2)
	z=0
	#if(r<1):
	z = (math.sqrt(-2*(math.log(v1))))*(math.cos(2*(math.pi)*v2))
	
	x= (z*q)+prom
	return x


def genera_discretaautos():
	#cantidad de autos = 50
	#prob de autos en senttido contrario 0.3
	n=10
	p=0.3
	a = random.random()
	i=0
	c= (p/(1-p))
	pr= (1-p)**(n)
	#(pr)
	F=pr
	while (a>=F):
		#(a)
		#(F)
		pr=((c*(n-i))/(i+1))*pr
		#(pr)
		F=F+pr
		#(F)
		i=i+1
		#(i)
		
	x=i
	return x


def genera_discretabache(d1,d2,d3,d4):
	u = random.random()
	if u<=d1:
		finv = 1
	elif u<=d1+d2:
		finv = 3
	elif u<=d1+d2+d3:
		finv = 6
	else:
		finv = 7
	return finv

# Creamos los sprites (clases) de los objetos del juego:

class Myauto(pygame.sprite.Sprite):

    #La bola y su comportamiento en la pantalla"
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagen).convert_alpha()
        #pygame.image.load("autoblanco.png").convert_alpha()
        self.rect = self.image.get_rect()
        #self.actions = {"0g":(45,75,20,20)}
        self.nombre="auto"
        self.rect.centerx = puntoinicialautox
        self.rect.centery = puntoinicialautoy
        self.speed = [velocidadautox, velocidadautoy]
        self.orientacion = 0
        self.var=0
        self.sentidogiro=1
        self.colisionado=0
        
	def movermiauto(self,c,py):
		self.rect.centery = py
		self.rect.centerx = c

    def update(self,x4,pos):
    	pyy=funcionmov(pos,(int(x4)))
    	self.rect.centery = pyy+self.var
    	self.rect.centerx = pos
    	if self.rect.right > SCREEN_WIDTH+110:
    		self.rect.centerx = 1500
    	if self.rect.left<-15:
    		self.speed[1] = 0
    	self.rect.move_ip((self.speed[0], self.speed[1]))

        #determinamos si la pelota choca con algo
    def colision(self, objetivo):
    	
    	if((self.sentidogiro)==-1):
        	if self.rect.colliderect(objetivo.rect):
        		self.colisionado=self.colisionado+0.1
        		nd=self.var+(random.randint(1, 3))
        		if (nd>40):
        			self.var=self.var+(random.randint(-3, -1 ))
        		else: 
        			self.var=nd
        		if(objetivo.nombre=="auto"):
        			mensajem="HAZ FALLADO"
        			print("han chocado dos autos")
        if((self.sentidogiro)==(1)):
        	if self.rect.colliderect(objetivo.rect):
        		self.colisionado=self.colisionado+0.1
        		nd=self.var-(random.randint(1, 3))
        		if (nd<-40):
        			self.var=self.var+(random.randint(1, 3 ))
        		else: 
        			self.var=nd
        		if(objetivo.nombre=="auto"):
        			mensajem="HAZ FALLADO"
        			print("Han chocado dos autos")
       	
        
        		
            
class Bache(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bache.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.nombre="bache"
        self.posx=x
        self.posy=y
        self.rect.centerx = x
        self.rect.centery = y
    
    


# ------------------------------
# Funcion principal del juego


def main():
    pygame.init() #inicializacion de todos los modulos
    pygame.mixer.init()
    pantalla=pygame.display.set_mode([1366,780],pygame.RESIZABLE)
    #determina el tamaño de ventana y crea una supeficie
    pygame.display.set_caption("SIMULACION")#titulo de la ventana

    fondo = pygame.image.load("mapa.jpg").convert()
    carretera1 = pygame.image.load("1curva.png").convert()
    carretera2 = pygame.image.load("2curvas.png").convert()
    carretera3 = pygame.image.load("3curva.png").convert()

    x2=str(genera_discretaautos())
    x1=str(genera_discretabache(0.5,0.1,0.3,0.1))

    x4=str( random.randint(1, 3))


    coche = Myauto("autoblanco.png")
    
    

    coches = []
    objects = []


    i=0
    for i in range(int(x1)):         # creamos 7 objetos
        pb=(random.randint(200, 1300))
        o = Bache((pb),((funcionmov(pb,(int(x4))))+(random.randint(-40,40))))
        objects.append(o)

    j=0
    for j in range(10):         # creamos 10 aautos
        li=(random.randint(0,2))
        o = Myauto(imagenes[li])
        coches.append(o)

    #salir= False
    reloj1=pygame.time.Clock() #iniciamos reloj
    pygame.key.set_repeat(1, 25) #activa la repeticion
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
    
    #x1=str(genera_discretabache(0.5,0.1,0.3,0.1))
    
    x3=str(genera_continuadistancia())
    #x5 velocidad del auto
    x5=200
    #x6 cantidad de gsolina
    x6=coche.colisionado
    

    texto2=fuente2.render(x1+" baches",0,(0,0,0))
    texto3=fuente2.render(x2+" autos en sentido contrario",0,(0,0,0))
    texto4=fuente2.render(x3+" km",0,(0,0,0))
    texto5=fuente2.render(x4+" curvas",0,(0,0,0))
    texto6=fuente2.render("Chevrolet Aveo: 14 km/litro",0,(0,0,0))
    texto7=fuente2.render("cantidad de gasolina= "+str(x6)+" litros",0,(0,0,0))
    
    #rotar_coche(coche,-10)
    #girar_coche(coche,"0g")
    j=0
    for j in range(int(x2)):         # creamos 7 objetos
	    rotar_coche(coches[j],180)
    
    

    j=int(x2)
    for j in range(10):         # creamos 7 objetos
    	coches[j].var=izquierda+(random.randint(20, 30 ))
    	coches[j].sentidogiro=1
	
	j=1
    for j in range(int(x2)):         # creamos 7 objetos
	    coches[j].var=derecha-(random.randint(10, 30 ))
	    coches[j].sentidogiro=-1
	    

    coche.var=izquierda+(random.randint(20, 30 ))
    coche.sentidogiro=1
   
    c=1
    
  
    while True:#loop principal
    	reloj1.tick(20) #reloj que actualiza la pantallla cada 20 frames
        pos_mouse=pygame.mouse.get_pos()
        mov_mouse=pygame.mouse.get_rel()
        
        textomensaje=fuente1.render(mensajem,0,(0,0,0))
    
        coche.update(x4,c)
        c=c+4

        j=int(x2)
    	for j in range(10):   
    		possx[j]=possx[j]+4
    		#c+(random.randint(10, 40 ))
	     	coches[j].update(x4,possx[j])


        j=0
    	for j in range(int(x2)):  
    	    posis[j]=posis[j]-4
    	    #(random.randint(10, 40 ))
    	    coches[j].update(x4,posis[j])
      
        if((coche.var>izquierda) and (coche.sentidogiro==1)):
        	coche.var=coche.var-6

      

        k=0
        for k in range(10): 
        	if((coches[k].var>izquierda) and (coches[k].sentidogiro==1)):
        		coches[k].var=coches[k].var-4

        	if((coches[k].var<derecha) and (coches[k].sentidogiro==-1)):
        		coches[k].var=coches[k].var+4
        
        
        

        j=0
        k=0
    	for j in range(10):   
    		for k in range(9):
    			if(k==j):
    				k=k+1
    			if(j!=k):
    				coches[j].colision(coches[k])
    		
    	

        j=0
        k=0
        for k in range(10):   
        	for j in range(int(x1)):
        		coche.colision(objects[j])
	     		coches[k].colision(objects[j])
	     		
    		
		if(c<SCREEN_WIDTH):
			x6=x6+coche.colisionado
			numcoli=((round (x6/10000)))
			gasolinatotal= float(x3)
			print ("gasolinatotal________________-")
			gasolinatotal = (gasolinatotal/14.0)+(numcoli*0.4)+(float(x4)*0.2)
			texto7=fuente2.render("cantidad de gasolina= "+str(gasolinatotal)+" litros",0,(0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type==pygame.KEYDOWN:
                if event.key==K_UP:
                	coche.rect.centery -= 5
                elif event.key==K_DOWN:
                	coche.rect.centery += 5
                elif event.key==K_ESCAPE:
                    sys.exit(0)
            elif event.type==pygame.KEYUP:
                if event.key==K_UP:
                	coche.rect.centery += 0
                elif event.key==K_DOWN:
                	coche.rect.centery += 0
        #si movemos el mouse mover la entidad a su posision
            #elif mov_mouse[1] != 0:
            	#coche.rect.centery = pos_mouse[1]
        

       	#pantalla.blit(fondo, (0,0))
       	pantalla.fill(blanco)
       	
       	#pantalla.blit(boton,(1250,10))
        

        #(x4)


        if((int(x4))==3):	    	
        	pantalla.blit(carretera3,(0,0)) 

        if((int(x4))==2):		
			pantalla.blit(carretera2,(0,0)) 	

        if((int(x4))==1): 	
       		pantalla.blit(carretera1,(0,0))
			


		        		
		pantalla.blit(texto1,(10,10))
        pantalla.blit(texto2,(10,35))
        pantalla.blit(texto3,(10,55))
        pantalla.blit(texto4,(10,75))
        pantalla.blit(texto5,(10,95))
        pantalla.blit(texto6,(10,115))
        pantalla.blit(texto7,(10,135))
         
    
    

        if((int(x1))==1):
            todos=pygame.sprite.RenderPlain(coche,objects[0],coches[0],coches[1],coches[2],coches[3],coches[4],coches[5],coches[6],coches[7],coches[8],coches[9])
        if((int(x1))==3):
            todos=pygame.sprite.RenderPlain(coche,objects[0],objects[1],objects[2],coches[0],coches[1],coches[2],coches[3],coches[4],coches[5],coches[6],coches[7],coches[8],coches[9])
        if((int(x1))==6):
            todos=pygame.sprite.RenderPlain(coche,objects[0],objects[1],objects[2],objects[3],objects[4],objects[5],coches[0],coches[1],coches[2],coches[3],coches[4],coches[5],coches[6],coches[7],coches[8],coches[9])
       	if((int(x1))==7):
            todos=pygame.sprite.RenderPlain(coche,objects[0],objects[1],objects[2],objects[3],objects[4],objects[5],objects[6],coches[0],coches[1],coches[2],coches[3],coches[4],coches[5],coches[6],coches[7],coches[8],coches[9])
        


        todos.draw(pantalla)
        pantalla.blit(texto1,(10,10)) 
        pantalla.blit(textomensaje,(1000,10))
        pygame.display.update() #refresca la pantalla
        pygame.display.flip()
        pantalla.blit(texto1,(10,10))
    #pygame.quit() #cierrra la ventana al presionar el boton x
	print (gasolinatotal)

if __name__ == "__main__":

    main()


