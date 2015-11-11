# -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Programacion 2 ----------
# -----------------------------------------------
# ----- Descripcion: Cliente socket CHAT
# -------------------------------------------------
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 10000))
print "Conectado!!"
while 1:
	s.send(raw_input("Cliente>> "))	
	print "Server>> " + s.recv(1000)
	
s.close()
