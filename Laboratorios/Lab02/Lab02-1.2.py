import serial

s = serial.Serial(0)	#COM1
s.baurate = 9600

f = open("datos.bin","wb")	# abre el archivo en modo escritura

dato = []
for i in range(100):	# espera los 10.000 datos
	a = s.readline()
	f.write(a)	
f.close()

#  =========== Archivo 
f = open("datos.bin","rb")
for l in f:
	dato.append(l[:-1])		# agrega datos al array
f.close()


a = 0.0
b = 0.0
c = 0.0
f = 0.0

for d in dato:	
	e = d.split(",")	# trozea la info
	a += int(e[0])
	b += int(e[1])
	c += int(e[2])
	f += float(e[3])
	print d			# imprime datos

print "\nPromedio a: " + str(a/len(dato))
print "Promedio b: " + str(b/len(dato))
print "Promedio c: " + str(c/len(dato))
print "Promedio f: " + str(f/len(dato))


