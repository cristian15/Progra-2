# -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Programacion 2 ----------
# -----------------------------------------------
# ----- Descripcion: Recive la direccion a mover 7 robots 
# -------------------------------------------------
import serial
import pygame
from pygame.locals import *

import random as RA

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
# Clase de Robot
#---------------------------------------------------------------------	
class Robot():
	def __init__(self, x, y, vel):
		self.x = x
		self.y = y
		self.vel = vel
	def display(self):
		wm.blit(Load_Image("robot.png", True), (self.x, self.y))
	def move(self, dir):	# mueve el robot segun la direccion 
		#print dir
		if dir == "N":
			self.y -= self.vel
		elif dir == "S":
			self.y += self.vel
		elif dir == "E":
			self.x += self.vel
		elif dir == "O":
			self.x -= self.vel
	def margin(self):		# comprueba que no salga de la pantalla
		if self.x > width - sizeRobots:
			self.x = width - sizeRobots
		elif self.x < 0:
			self.x = 0
		if self.y > height - sizeRobots:
			self.y = height - sizeRobots
		elif self.y < 0:
			self.y = 0
			

	
	
s = serial.Serial(0)	#COM1
s.baurate = 2400
	
pygame.init()
(width, height)  = (640, 480)	# dimenciones de la ventana

wm = pygame.display.set_mode((width, height))
pygame.display.set_caption('Robots')
clock = pygame.time.Clock()

robots = []
nRobosts = 7		# numero de Robots a dibujar
sizeRobots = 32		# tamanio de la imagen robot

# instancia los robots
for i in range(nRobosts):
	x = RA.randint(sizeRobots, width - sizeRobots)
	y = RA.randint(sizeRobots, height - sizeRobots)
	r = Robot(x, y, 2)
	robots.append(r)
	
lok = True

while lok:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			lok = False
	wm.fill((100,100,50))	# pinta el fondo
	
	i = 1
	for r in robots:
		s.write(str(i)+"\n")	#envia el identificador del script Slave		
		comm = s.readline()
		r.move(comm[:-1])	# mueve segun el comando recivido
		r.margin()
		r.display()
		print "move r"+str(i)
		i+=1
	
	pygame.display.flip()	#actualiza la pantalla
	clock.tick(100)	
s.close()
pygame.quit()