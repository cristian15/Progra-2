# -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Programacion 2 ----------
# -----------------------------------------------
# ----- Descripcion: Recive el nombre de la tabla y el codigo del producto
# ------------------ para mostrar la informacion de las ventas
# -------------------------------------------------

import sqlite3
import serial

# conexion a la BD
conn = sqlite3.connect("mybd.db")
cur = conn.cursor()


s = serial.Serial(2)	# COM3
s.baurate = 2400

while 1:
	comm = s.readline()		# recive la informacion  
	print comm
	t = comm.split("&")		# trozea la informacion 
	query = "SELECT ic, ip, iq, it FROM "+t[0] +" WHERE ic = "+t[1]
	a = cur.execute(query)
	arrayVentas  = a.fetchall()		# toma todas las ventas 
	print "|\tID\t|\tCodigo\t|\tPrecio\t|\tCantidad\t|\tFecha|"
	tVentas = 0
	for ventas in arrayVentas:
		print "|\t"+str(ventas[0])+"\t|\t"+str(ventas[1])+"\t|\t"+str(ventas[2])+"\t|\t"+str(ventas[3])+"\t|\n"
		tVentas += int(ventas[1])*int(ventas[2])
		s.write("|\t"+str(ventas[0])+"\t|\t"+str(ventas[1])+"\t|\t"+str(ventas[2])+"\t|\t"+str(ventas[3])+"\t|\n")
	s.write("Total Productos: "+ str(len(arrayVentas))+"\n")
	s.write("Total Ventas: $"+ str(tVentas)+"\n")
	print "Total Productos: "+ str(len(arrayVentas))
	print "\nTotal Ventas: $"+ str(tVentas)
cur.close()