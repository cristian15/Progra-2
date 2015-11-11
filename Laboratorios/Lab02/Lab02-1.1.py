import random as RA
import time
import serial

s = serial.Serial(0)	#COM1
s.baurate = 9600
for i in range(10000):
	a =  str(RA.randint(1,100)) + "," + str(RA.randint(1,1000)) +","+ str(RA.randint(1,10000)) +","+str(RA.random())
	s.write(a+"\n")
	#print a
	time.sleep(.1)	# espera .1 segundos
 