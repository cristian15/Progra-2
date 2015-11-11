# -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Programacion 2 ----------
# -----------------------------------------------
# ----- Descripcion: Envia la informacion de la tabla y el codigo del producto
# -------------------------------------------------
import serial

s = serial.Serial(2)		#COM3
s.baurate = 2400

tabla = raw_input("Ingresa Tabla: ")
id = raw_input("Ingresa ID: ")
s.write(tabla+"&"+id+"\n")

while 1:
	print s.readline()