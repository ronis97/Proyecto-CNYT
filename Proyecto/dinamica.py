import complejos as comp
import vectmatrices as vmat
import numpy as np
import matplotlib.pyplot as plt


def label(l):
    lista = []
    for i in range(len(l)):
        lista.append("Pto."+" "+str(i))
    return lista
def estados(V):
    l = []
    for i in range(len(V)):
        #print(V[i][0][0])
        l.append(V[i][0][0])
    return l
def proceso(V,Matriz,clicks):
    

    res = vmat.generar(len(V),len(Matriz[0]))
    res = vmat.multiplicarmatriz(Matriz,V)

    if clicks == 0:
        return V
    else:
        
        for i in range(clicks-1):
            res = vmat.multiplicarmatriz(Matriz,res)
        return res
def mostrar(index,estado,labels,clicks):

    plt.bar(index,estado)
    plt.xlabel('Estado')
    plt.ylabel('Valor')
    plt.xticks(index,labels,rotation = 75)
    plt.title("Evoucion dinamica del sistema despues de "+str(clicks)+" clicks de tiempo")
    plt.show()   
def main(M,V,clicks = 0):
    

    res = proceso(V,M,clicks)
    print(res)
    modulo = vmat.modulomatriz(res)
    print(modulo) 
    labels = label(V)
    estado = estados(modulo)

    index = np.arange(len(labels))
   
    mostrar(index,estado,labels,clicks)
    print(estado)

    
##main()


