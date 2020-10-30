import numpy as np
import cv2
def convulucion(A,B):
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

imagen = cv2.imread('003.jpg')
imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
imagen = cv2.resize(imagen,(256,256))





matriz=[img_final]
filtro=[[1,1,1],[1,0,1],[1,1,1]]

A=np.array(matriz)
B=np.array(filtro)

#C=np.zeros((2,2))

resultado=convulucion(A,B)
final=cv2.imwrite('convolucion.jpg',resultado)
