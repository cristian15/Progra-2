# -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Programacion 2 ----------
# -----------------------------------------------
# ----- Descripcion: Sube imagenes desde una carpeta a SQLite 
# -------------------------------------------------
import sqlite3
import os
import random as RA

# ---------- Devuelve una fecha aleatoria --------------
def randFecha():		
	fecha = ""
	fecha += str(RA.randint(1, 31)) 
	fecha += '-' + str(RA.randint(1, 12))
	fecha += '-' + str(RA.randint(2000,2030))
	return fecha
# ---------- Devuelve una hora aleatoria -----------------
def randHora():
	hora = ""
	hora += str(RA.randint(0, 23)) 
	hora += ':' + str(RA.randint(0, 59))
	hora += ':' + str(RA.randint(0,59))
	return hora
	
# ----------- Sube la Imagen a la BD --------------------------
def upImageDB(dirImage):
	img = open(dirImage, 'rb').read()
	buff = sqlite3.Binary(img)
	try:
		conn = sqlite3.connect("Base Datos\\datos.db")
		cur = conn.cursor()
		cur.execute("INSERT INTO fotos(fecha, hora, img) VALUES('"+ randFecha() +"', '"+ randHora() +"', ?)", (buff,))
		conn.commit()
		cur.close()
		conn.close()
	except:
		print "Error DB"
	
for files in os.listdir("IMAGENES\\"):
    if files.endswith(".jpg"):
		print files
		upImageDB("IMAGENES\\"+files)


