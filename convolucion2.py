# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:16:28 2020

@author: User
"""
import numpy as np
import cv2
def convulucion(A,B):  #SIN PADDING
    C=np.zeros((len(A)-2,len(A[0])-2))
    suma=0
    for i in range(len(C)):
        for j in range(len(C[0])):
            res=0
            for m in range(len(B)):
                for n in range(len(B[0])):
                    suma+= A[m+i][j+n]*B[m][n]
            C[i][j]= suma
            suma=0
    return C

def esc_grises(imagen):
    R = 0.21
    G = 0.07
    B = 0.72
    s = 0
    Img_gris = np.zeros((len(imagen),len(imagen[0])))
    for i in range(0,len(imagen)):
        for j in range(0,len(imagen[0])):
            for a in range(0,3):
                if a == 0:
                    s += imagen[i][j][a]*R
                    a = 1
                elif a == 1:
                    s += (imagen[i][j][a]*G)
                    a = 2
                elif a == 2:
                    s += imagen[i][j][a]*B
                    a = 0
            Img_gris[i][j]=s
            s = 0
    return Img_gris

def agregar_padding(A):  #SIN PADDING
    B = np.zeros((len(A)+2,len(A[0])+2))
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[i+1][j+1]=A[i][j]
    return B

def HEEHEE (A):
    B = np.zeros((len(A),len(A[0])))
    for i in range(0,len(A)):
        for j in range(0,len(A[0])):
            if A[i][j] < 128:
                B[i][j] = 0
            elif A[i][j] > 128:
                B[i][j] = 255
    return B
                
                
            


imagen = cv2.imread('imagen_prueba.jpg')
imagen=cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)


Matriz=esc_grises(imagen)
print(Matriz)
img_gris = cv2.imwrite('grises.jpg',Matriz)
Filtro=[[1,1,1],[1,0,1],[1,1,1]]
img_conv=convulucion(Matriz, Filtro)
padding = agregar_padding(Matriz)
pad = convulucion(padding, Filtro)
heehee= HEEHEE(Matriz)
img_padding = cv2.imwrite('padding.jpg',pad)
conv = cv2.imwrite('convolucion.jpg',img_conv)
BN= cv2.imwrite('BN.jpg',heehee)


