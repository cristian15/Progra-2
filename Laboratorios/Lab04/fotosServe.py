# -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Programacion 2 ----------
# -----------------------------------------------
# ----- Descripcion: Server Socket recive fotos  
# ----------------- y las muestra mediante pygame
# -------------------------------------------------
import socket
import pygame
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("localhost", 10000))	# Socket
print "Esperando Conexion..."
s.listen(1)		#conexiones esperando escuchar
sClient, addr = s.accept()
print "Conexion aceptada"

def Load_Image(sFile,transp=False):
    try: image = pygame.image.load(sFile)
    except pygame.error,message:
           raise SystemExit,message
    image = image.convert()
    if transp:
       color = image.get_at((0,0))
       image.set_colorkey(color,RLEACCEL)
    return image


pygame.init()
nSize=[200,200]
Black = [0,0,0]
Sc = pygame.display.set_mode(nSize)
pygame.display.set_caption("Imagenes Sockets")

lOK = True
while lOK:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: lOK = False
	imgString = sClient.recv(200000)
	if imgString == "END":		# comando de termino
		break
	size = sClient.recv(1000).split("x")
	print size
	imgSurf = pygame.image.fromstring(imgString,(int(size[0]),int(size[1])),"RGB")		# recive la imagen como string
	pygame.image.save(imgSurf, "img.jpg")			# guarda la imagen
	
	Img = Load_Image("img.jpg")		
	Img = pygame.transform.scale(Img,(200,200))		#resizea la imagen
	
	Sc.fill(Black)		
	Sc.blit(Img,(0,0))	
	pygame.display.flip()
	os.remove("img.jpg")	
s.close()