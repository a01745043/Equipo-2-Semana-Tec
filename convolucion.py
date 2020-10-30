import numpy as np
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

matriz=[[6,9,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
filtro=[[1,0,2],[5,0,9],[6,2,1]]

A=np.array(matriz)
B=np.array(filtro)

#C=np.zeros((2,2))

resultado=convulucion(A,B)
print(resultado)