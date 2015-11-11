# -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Programacion 2 ----------
# -----------------------------------------------
# ----- Descripcion: Cliente Socket envia fotos 
# ------------------ tomadas de una carpeta
# -------------------------------------------------
import socket
import os
import pygame
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 10000))

print "Conectado!!"


# ---- Busca las imagenes en la carpeta ----------
for files in os.listdir("Imagenes\\"):
    if files.endswith(".jpg"):
		imgSurf = pygame.image.load("Imagenes\\"+files)
		imgString = pygame.image.tostring(imgSurf,"RGB")
		size = imgSurf.get_size()
		s.send(imgString)		# envia foto como String
		
		time.sleep(1)		# espera
		s.send(str(size[0])+"x"+str(size[1]))
		print "size "+str(size[0])+"x"+str(size[1])+" - "+files + " enviada!!"
s.send("END")		#envia termino de imagenes
s.close()

