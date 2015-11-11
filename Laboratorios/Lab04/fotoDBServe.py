# -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Programacion 2 ----------
# -----------------------------------------------
# ----- Descripcion: Server Socket recive fotos  
# ----------------- y las inserta a una Base de Datos
# -------------------------------------------------
import socket
import pygame
import sqlite3
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("localhost", 10000))	# Socket
print "Esperando Conexion..."
s.listen(1)		#conexiones esperando escuchar
sClient, addr = s.accept()
print "Conexion aceptada"


# Crea Tabla Img
conn = sqlite3.connect("Fotos.db")
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Img ')		# Elimina la tabla si es q existe
cur.execute('CREATE TABLE Img (id INTEGER PRIMARY KEY AUTOINCREMENT, im BLOB )')	# Crea la tabla
conn.commit()
cur.close()
conn.close()


# ----------- Sube la Imagen a la BD --------------------------
def upImageDB(dirImage):
	img = open(dirImage, 'rb').read()
	buff = sqlite3.Binary(img)
	try:
		conn = sqlite3.connect("Fotos.db")
		cur = conn.cursor()
		cur.execute("INSERT INTO Img(im) VALUES(?)", (buff,))
		conn.commit()
		cur.close()
		conn.close()
	except:
		print "Error DB"
		
# ------------------------------------------
# ---- Recive las fotos por socket y las sube a la BD
# ----------------------------------------------
while 1:
	imgString = sClient.recv(200000)
	if imgString == "END":		# comando de termino
		break
	size = sClient.recv(1000).split("x")
	print size
	imgSurf = pygame.image.fromstring(imgString,(int(size[0]),int(size[1])),"RGB")		# recive la imagen como string
	pygame.image.save(imgSurf, "img.jpg")			# guarda la imagen
	upImageDB("img.jpg")
	


s.close()