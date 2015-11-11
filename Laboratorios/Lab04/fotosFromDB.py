# -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Programacion 2 ----------
# -----------------------------------------------
# ----- Descripcion: Muestra en pygame fotos tomadas 
# ------------------ desde Base de Datos
# -------------------------------------------------
import pygame
import sqlite3
import time
import os

def Load_Image(sFile,transp=False):
    try: image = pygame.image.load(sFile)
    except pygame.error,message:
           raise SystemExit,message
    image = image.convert()
    if transp:
       color = image.get_at((0,0))
       image.set_colorkey(color,RLEACCEL)
    return image

# ------------------------------------------
# ---- Obtiene las fotos desde la base de datos
# ----------------------------------------------
conn = sqlite3.connect("Fotos.db")
cur = conn.cursor()
fotos = cur.execute("SELECT im FROM Img")	# obtiene todas las fotos desde la BD



pygame.init()
nSize=[200,200]
Black = [0,0,0]
Sc = pygame.display.set_mode(nSize)
pygame.display.set_caption("Imagenes from SQLite")

lOK = True

while lOK:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: lOK = False		
	for i in fotos:
		f = open("a.jpg","wb")
		f.write(i[0])
		f.close()
		Img = pygame.image.load("a.jpg")
		#Img = pygame.image.frombuffer(i,(64,64),"RGB")		
		Img = pygame.transform.scale(Img,(200,200))		#resizea la imagen	
		Sc.fill(Black)		
		Sc.blit(Img,(0,0))	
		pygame.display.flip()
		time.sleep(1)
		os.remove("a.jpg")
	print "Fin de filas"
conn.close()