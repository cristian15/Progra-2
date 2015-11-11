 # -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Programacion 2 ----------
# -----------------------------------------------
# ----- Descripcion: Muestra imagen en pygame desde SQLite
# -------------------------------------------------

import sqlite3
import pygame


def Load_Image(sFile, transp=False):
    try: image = pygame.image.load(sFile)
    except pygame.error,message:
           raise SystemExit,message
    image = image.convert()
    if transp:
       color = image.get_at((0,0))
       image.set_colorkey(color,RLEACCEL)
    return image
	
# ---------- Obtiene la foto desde la BD
def getImage(id):	
	conn = sqlite3.connect("Base Datos\\datos.db")
	cur = conn.cursor()
	a = cur.execute("SELECT img FROM fotos WHERE id = "+id)
	img = a.fetchone()
	if(img):
		f = open('foto.jpg','wb')
		f.write(img[0])
		f.close()
		conn.commit()
		cur.close()
		conn.close()
		return True
	else:
		print "No existe"
		return False
	
	
pygame.init()
nSize=[400,400]
Black = [0,0,0]
Sc = pygame.display.set_mode(nSize)
pygame.display.set_caption("Imagenes SQLite")

Img = Load_Image("foto.jpg")
Img = pygame.transform.scale(Img,(200,200))
lOK = True
while lOK:
	idFoto = raw_input("Ingresa ID de la foto: ")
	getImage(idFoto)
	Img = Load_Image("foto.jpg")
	Img = pygame.transform.scale(Img,(200,200))
	for event in pygame.event.get():
		if event.type == pygame.QUIT: lOK = False
	Sc.fill(Black)
	Sc.blit(Img,(30,30))
	pygame.display.flip()