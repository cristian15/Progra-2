 # -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Programacion 2 ----------
# -----------------------------------------------
# ----- Descripcion: Operaciones sobre tabla ventas en SQLite
# -------------------------------------------------

import sqlite3
import locale
import datetime

locale.setlocale(locale.LC_ALL,'')

# ----------------- Calcula el total de ventas entre las fechas recividas -----------
def getVentasFecha(fInicio, fFinal):	
	ventas = 0
	fInicio = fInicio.split("-")
	fFinal = fFinal.split("-")
	
	fechaInicio = datetime.datetime(int(fInicio[2]), int(fInicio[1]), int(fInicio[0]))
	fechaFin = datetime.datetime(int(fFinal[2]), int(fFinal[1]), int(fFinal[0]))
	for r in arrayVentas:
		p = r[2].split("-")
		try:
			fecha = datetime.datetime(int(p[2]), int(p[1]), int(p[0]))
		except:
			print str(p) +" No Existe"
		if  (fecha > fechaInicio ):
			if fecha < fechaFin:
				#print "as"
				ventas += float(r[0])
	ventas = locale.currency(ventas, grouping=True)
	return str(ventas)[:-1]

# conexion a la BD
conn = sqlite3.connect("Base Datos\\datos.db")
cur = conn.cursor()
a = cur.execute("SELECT v, t, f FROM ventas")
arrayVentas  = a.fetchall()		# toma todas las ventas 

ventasTotal = 0
ventasEfectivo = 0
ventasCheque = 0
ventasMaster = 0
ventasVisa = 0
for r in arrayVentas:
	ventasTotal += float(r[0]) 
	if str(r[1]) == "E":
		ventasEfectivo += float(r[0])		
	if str(r[1]) == "C":
		ventasCheque += float(r[0])
	if str(r[1]) == "M":
		ventasMaster += float(r[0])
	if str(r[1]) == "V":
		ventasVisa += float(r[0])

# -------------- Da el formato de dinero para mostrar 
ventasTotal = locale.currency(ventasTotal, grouping=True)
ventasEfectivo = locale.currency(ventasEfectivo, grouping=True)
ventasCheque = locale.currency(ventasCheque, grouping=True)
ventasMaster = locale.currency(ventasMaster, grouping=True)
ventasVisa = locale.currency(ventasVisa, grouping=True)


print "Total Ventas:   $" + str(ventasTotal)[:-1]
print "Total Ventas E: $" + str(ventasEfectivo)[:-1]
print "Total Ventas V:   $" + str(ventasVisa)[:-1]
print "Total Ventas M: $" + str(ventasMaster)[:-1]
print "Total Ventas C:   $" + str(ventasCheque)[:-1]

ok = True
while ok:
	fechaInicio = raw_input("Ingresa fecha Inicio (dd-mm-aaaa) [Salir = X]: ")
	if(fechaInicio == 'X' or fechaInicio == 'x'):
		ok= False
		break
	fechaFin = raw_input("Ingresa fecha Final (dd-mm-aaaa): ")
	print "Total ventas entre fechas: " + getVentasFecha(fechaInicio, fechaFin)