# By Alberto Caro S.
# Ing. Civil en Computacion
# Doctor(c) Cs. de la Computacion
# Pontificia Universidad Catolica de Chile
#-------------------------------------------

from PIL import Image
from pygame.locals import *
import pygame as pg, random as ra, time as ti

nRES = (469,83) ; lOK = True ; PATH = '.'

#---------------------------------------------------------------------
# Carga imagenes y convierte formato PyGame
#---------------------------------------------------------------------
def Load_Image(sFile,transp = False):
    try: image = pg.image.load(sFile)
    except pg.error,message:
           raise SystemExit,message
    image = image.convert()
    if transp:
       color = image.get_at((0,0))
       image.set_colorkey(color,RLEACCEL)
    return image

#---------------------------------------------------------------------
# Inicializa PyGames.-
#---------------------------------------------------------------------
def PyGame_Init():
    pg.init()
    pg.display.set_caption('PYGAME + PIL - By Alberto Caro - 2015()')
    return pg.display.set_mode(nRES)

#---------------------------------------------------------------------
# Pinta la Pantalla Principal de PyGames.-
#---------------------------------------------------------------------
def Pinta_Panel():
    Panta.blit(Panel,(0,0))
    return

#---------------------------------------------------------------------
# Pinta Proyectil en Panta.-
#---------------------------------------------------------------------
def PIL2PYG(aE):
    aXY = [(7,9),(72,9),(137,9),(202,9),(267,9),(332,9),(397,9)]
    for nPos in range(7):
     Data = aE[nPos][3]
     Size = aE[nPos][0]
     Mode = aE[nPos][2][0] + aE[nPos][2][1] + aE[nPos][2][2]
     i = pg.image.fromstring(Data,Size,Mode)
     Panta.blit(i,aXY[nPos])
    return

#---------------------------------------------------------------------
# Sacamos la informacion de imagenes a texto en tupla.-
#---------------------------------------------------------------------
def ToPIL(aF):
    aData = []
    for e in aF:
        i = Image.open(e)
        s = i.size
        f = i.format
        b = i.getbands()
        t = i.tostring()
        aData.append((s,f,b,t))
    return aData

#---------------------------------------------------------------------
# While Principal del Demo.-
#---------------------------------------------------------------------
Panta = PyGame_Init()
Panel = Load_Image('panel.png')
aFig  = ['a.jpg','b.jpg','c.jpg','d.jpg','e.jpg','f.jpg','g.jpg']

Fps = pg.time.Clock()

while lOK:
 ra.shuffle(aFig)
 cKey = pg.key.get_pressed()
 if cKey[pg.K_ESCAPE] : lOK = False
 ev = pg.event.get()
 for e in ev:
  if e.type == QUIT:
     lOK = False
 Pinta_Panel()
 aD = ToPIL(aFig)
 PIL2PYG(aD)
 Fps.tick(8)
 pg.display.flip()
pg.quit





