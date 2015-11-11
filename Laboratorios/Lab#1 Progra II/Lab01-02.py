 # -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Programacion 2 ----------
# -----------------------------------------------
# ----- Descripcion: Inserta datos a SQLite leidos desde un archivo
# -------------------------------------------------

import sqlite3

def putData(dato):		# inserta el dato en la tabla ventas reciviendo un array 
	conn = sqlite3.connect("Base Datos\\datos.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO ventas(p, q, v, f, t) VALUES("+dato[0]+","+dato[1]+" , "+dato[2]+", '"+dato[3]+"', '"+dato[4]+"')") 
	conn.commit()
	cur.close()
	conn.close()
f = open("movi.txt")
i=1;
for linea in f:
	putData(linea[:-1].split("&")) # trozea la linea para separar los datos para pasarlos a la funcion. quita el salto de linea
	print str(i) + " " + str(linea)
	i +=1