# -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Programacion 2 ----------
# -----------------------------------------------
# ----- Descripcion: Envia una direccion aleatoria para mover el robot
# -------------------------------------------------
import serial
import random as RA
import time


dirs = ("N","S","E","O","NM")
idSlave = "4"		#identificador del script

s = serial.Serial(1)	#COM2
s.baurate = 2400
while 1:
	comm = s.readline()
	print comm
	if comm[:-1] == idSlave:		
		f = dirs[RA.randint(0,4)]+"\n"
		s.write(f)	
		print f
	time.sleep(.05)
s.close()