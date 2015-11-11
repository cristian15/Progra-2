 # -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Programacion 2 ----------
# -----------------------------------------------
# ----- Descripcion: Movimiento aleatorio de naves en Pygame
# -------------------------------------------------

import pygame
from pygame.locals import *
import random

nMAX_SPRITES = 10 # numero de naves

#---------------------------------------------------------------------
# Carga imagenes y convierte formato pygame
#---------------------------------------------------------------------
def Load_Image(sFile,transp=False):
    try: image = pygame.image.load(sFile)
    except pygame.error,message:
           raise SystemExit,message
    image = image.convert()
    if transp:
       color = image.get_at((0,0))
       image.set_colorkey(color,RLEACCEL)
    return image

#---------------------------------------------------------------------
# Carga imagenes a array de sprites
#---------------------------------------------------------------------
def Set_Img():		#carga las imagenes, fondo y naves
    aImg = []
    aImg.append(Load_Image('bg.jpg' ))
    aImg.append(Load_Image('n2.png',True ))
    return aImg

#---------------------------------------------------------------------
# Pinta Fondo
#---------------------------------------------------------------------
def Draw_Bg():
    wm.blit(aFig[0],(0,0))
    return

#---------------------------------------------------------------------
# Main.-
#---------------------------------------------------------------------
pygame.init()

aSize  = [500,600] ; Black  = [0,0,0] ; aNaves = [] ; lok = True; nSel = 1

wm = pygame.display.set_mode(aSize)
pygame.display.set_caption('Mini Games')

clock = pygame.time.Clock()
aFig = Set_Img()
oxNaves = []
oyNaves = []
# ------------ Setea las posiciones iniciales de las naves -------------------
for i in range(nMAX_SPRITES):
	x = random.randrange(0,440)
	y = random.randrange(0,aSize[1])
	aNaves.append([x,y])
	sentido = random.randint(-1,1)
	while sentido == 0:		# Sentido a donde se mueve la nave
		sentido = random.randint(-1,1)
	oxNaves.append(sentido)
	sentido = random.randint(-1,1)
	while sentido == 0:		# Sentido a donde se mueve la nave
		sentido = random.randint(-1,1)
	oyNaves.append(sentido)

while lok:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			lok = False
	Draw_Bg()		#pinta el fondo
	for i in range(len(aNaves)):		# movimiento de las naves
		wm.blit(aFig[nSel],aNaves[i])
		aNaves[i][1] += random.randint(1,2) * oyNaves[i]	# coordenada Y
		aNaves[i][0] += random.randint(1,2) * oxNaves[i]	# coordenada X
		
		if aNaves[i][1] > aSize[1]:				# si sale de la pantalla
			aNaves[i][1] = -55
		if aNaves[i][0] > aSize[0]:				# si sale de la pantalla
			aNaves[i][0] = -60
		
		if aNaves[i][1] < -55:				# si sale de la pantalla
			aNaves[i][1] = aSize[1]
		if aNaves[i][0] < -60:				# si sale de la pantalla
			aNaves[i][0] = aSize[0]
			
		
	pygame.display.flip()	#actualiza la pantalla
	clock.tick(100)
pygame.quit ()