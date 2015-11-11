# -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Programacion 2 ----------
# -----------------------------------------------
# ----- Descripcion: Servidor socket CHAT
# -------------------------------------------------
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("localhost", 10000))	# Socket
print "Esperando conexion..."
s.listen(1)		#conexiones esperando escuchar
sClient, addr = s.accept()
print "Conexion aceptada!!"
while 1:
	msje = sClient.recv(1000)
	print "Cliente>> " + msje
	sClient.send(raw_input("Server>> "))
s.close()