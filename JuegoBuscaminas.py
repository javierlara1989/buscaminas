# -*- coding: cp1252 -*-

# BLOQUE DE DEFINICIÓN

# DEFINICIÓN DE CONSTANTES

# IMPORTACIÓN DE FUNCIONES
from random import randrange


# DEFINICIÓN DE FUNCIONES
def cuenta (x,y):
    suma = 0
    for a in range (x-1,x+2):
        for b in range (y-1,y+2):
            if a>=0 and a<=l_matriz-1 and b>=0 and b<=l_matriz-1:
                if matriz[a][b]=="*":
                    suma = suma + 1
    return suma

def print_matriz (a):
    print "\n"
    for x in a:
        for y in x:
            print y," ",
        print "\n"

print "###################################################################"
print "#################     Reglas:   ###################################"
print "###################################################################"
print "#####     Ganas:                                      #############"
print "##### a) Si descubres la posicion de todas las minas  #############"
print "###################################################################"
print "#####     Pierdes:                                           ######"
print "#####    a) Si pisas una mina                                ######"
print "#####    b) Si fallas al indicar la posicion de una mina     ######"
print "###################################################################\n"
print "Niveles:"
print "1 Fácil.- 8x8 - 10 minas"
print "2 Intermedio.- 16x16 - 40 minas"
print "3 Avanzado.- 16x30 - 90 minas\n"

while (True):
    lvl = input ("Ingresa el nivel seleccionado\n")
    if(lvl == 1):
        l_matriz = 8
        minas = 10
        break
    if(lvl == 2):
        l_matriz = 16
        minas = 40
        break
    if(lvl == 3):
        l_matriz = 30
        minas = 90
        break
    else:
        print "Caracter ingresado no valido, intenta nuevamente\n"
 

matriz = []
for A in range (l_matriz):
    matriz2 = []
    for B in range (l_matriz):
        matriz2.append (0)
    matriz.append (matriz2)

matriz2 = []
for A in range (l_matriz):
    matriz3 = []
    for B in range (l_matriz):
        matriz3.append ("#")
    matriz2.append (matriz3)

suma = 0
while suma!=minas:
    random1 = randrange(0,l_matriz)
    random2 = randrange(0,l_matriz)
    if matriz[random1][random2] != '*':
        matriz[random1][random2] = '*'
        suma = suma + 1

for C in range (l_matriz):
    for D in range (l_matriz):
        e = cuenta(C,D)
        if matriz[C][D]!="*":
            matriz[C][D]=e
 
suma = 0
while suma!=minas:
    print "\n"
    print "========================================================================"

    z = raw_input ("Escribe MINA en caso que encuentres una o en caso contrario presiona Enter  ")
    if z=="MINA":
        print "Ingresa coordenadas de un lugar con minas"
        y2 = input ("   Ingresa coordenada x:  ") -1
        x2 = input ("   Ingresa coordenada y:  ") -1
        if matriz[x2][y2]=="*":
            suma = suma + 1
            matriz2[x2][y2]="*"
            if suma==minas:
                print_matriz (matriz2)
                print "Felicidades. Has ganado"
                break
            
        else:
            print_matriz (matriz)
            print "Has perdido"
            break
    print "Ingrese coordenadas de un lugar sin minas"
    y = input ("    Ingresa coordenada x:   ") -1
    x = input ("    Ingresa coordenada y:   ") -1
    if matriz[x][y]!="*":
        matriz2[x][y]=matriz[x][y]
    else:
        print_matriz (matriz)
        print "Has perdido"
        break
    print_matriz (matriz2)
    print "Aun te quedan",minas-suma,"minas por descubrir"
print "\n"
asdf = input ("Apreta un boton para cerrar")

#NOTA IMPORTANTE
#-El nivel 3 no está terminado aún

