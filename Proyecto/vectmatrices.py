"""Libreria de operaciones entre matrices o vectores compuestos por numeros
complejos, requiere de la libreria anterior (complejos) para poder hacer uso
de todas las funciones"""
import complejos as comp
import math
def generar(n,m):
    """Genera una matriz con arreglos vacios de tamaño n x m"""
    ma = []
    for i in range(n):
        l = []
        for j in range(m):
            l.append([0,0])
        ma.append(l)
    return ma

def generaridentidad(n):
    """Genera una matriz identidad
    (compuesta de numeros complejos) de tamaño n"""
    ma = []
    for i in range(n):
        l = []
        for j in range(n):
            if i == j:
                l.append([1,0])
            else:
                l.append([0,0])
        ma.append(l)
    return ma
            
def sumamatriz(matriz1,matriz2):
    """Recibe dos matrices o vectores y los suma, estos deben tener
    el mismo tamaño m x n y deben contener arreglos"""
    res = generar(len(matriz1),len(matriz1[0]))
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            res[i][j] = comp.suma(matriz1[i][j],matriz2[i][j])
    return res
def restamatriz(matriz1,matriz2):
    """Recibe dos matrices o vectores y los resta, estos deben tener
    el mismo tamaño m x n y deben contener arreglos"""
    res = generar(len(matriz1),len(matriz1[0]))
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            res[i][j] = comp.resta(matriz1[i][j],matriz2[i][j])
    return res

def multiplicarmatriz(matriz1,matriz2):
    #print("longitud1",len(matriz1))
    #print("longitud2",len(matriz2))
    """La funcion accion es un caso especial de esta funcion donde la matriz2 es un vector,
    se realiza la verificacion por medio del condicional
    Multiplica dos matrices complejas, es de resaltar que cada elemento de las
    matrices involucradas debe ser un arreglo denotando un numero complejo"""
    ##GUIA m[i][j] = m[i][j] + m1[i][k]* m2[k][j]
    if len(matriz1[0]) == len(matriz2):
        res = generar(len(matriz1),len(matriz2[0]))
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] = [0,0]
                for k in range(len(matriz2)):
                    res[i][j] = comp.suma(res[i][j],#
                                comp.multiplicar(matriz1[i][k],matriz2[k][j]))
        if len(res) == 1:
            return res[i][j]
        return res
    else:
        return 0

def mostrar(matriz):
    """Muestra la matriz en pantalla, en caso de no encontrar una,
    indica error"""
    if type(matriz) is list:
        for i in matriz:
            print(*i)
    else:
        print("Error. Las matrices no tienen dimensiones compatibles")
    
def inversoadimatriz(matriz):
    """Recibe una matriz o un vector y halla el inverso aditiva de este(a)"""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = comp.inversoaditivo(matriz[i][j])
    return matriz

def multescalarmatriz(escalar,matriz):
    """Multiplicar un numero complejos (escalar) con una matriz o vector """
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = comp.escalarpornum(escalar,matriz[i][j])
    return matriz

def transpuesta(matriz):
    """Genera la transpuesta de un vector o matriz dado"""
    res = generar(len(matriz[0]),len(matriz))
    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            res[i][j] = matriz[j][i]
##        print("transpuesta")
##        print(res)
    return res

def conjugadamatriz(matriz):

    """Halla el conjugado de una matriz """    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = comp.conjugado(matriz[i][j])
    return matriz

def adjuntamatriz(matriz):
    """Halla la adjunta de una matriz calculando la transpuesta y luego
    la conjugada"""
    transpuest = transpuesta(matriz)
    conjugada = conjugadamatriz(transpuest)
    return transpuest

def productinterno(vector1,vector2):
    """Halla el producto interno de dos vectores compuesto de complejos"""
    daga = adjuntamatriz(vector1)
    res = multiplicarmatriz(daga,vector2)
    if res[1] == 0:
        return res[0]
    return res

def normavector(vector1):
    """Halla la norma de un vector compuesto de complejos"""
    res = productinterno(vector1,vector1)
    res = res ** 0.5
    return res

def distanciavectores(vector1,vector2):
    """Halla la distancia entre dos vectores compuesto de complejos"""
    resta = restamatriz(vector1,vector2)
    res = normavector(resta)
    return res

def matrizhermitiana(matriz1):
    """Comprueba si una matriz es hermitiana"""
    daga = adjuntamatriz(matriz1)
    if daga == matriz1:
        return True
    return False

def truncar(matriz):
    """Trunca los valores reales en la matriz, sean de la parte real o de la
    parte imaginaria"""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            for k in range(2):
                matriz[i][j][k] = math.ceil(matriz[i][j][k])
    return matriz

def matrizunitaria(matriz):
    """Comprueba si una matriz es unitaria"""
    daga = adjuntamatriz(matriz)
    res = multiplicarmatriz(matriz,daga)
    res = truncar(res)
    identidad = generaridentidad(len(matriz))
    if res == identidad:
        return True
    return False

def productotensorial(matriz1,matriz2):
    """Halla el producto rensorial de dos matrices compuestas de complejos"""
    res = generar(len(matriz1)*len(matriz2),len(matriz1[0])*len(matriz2[0]))
    m = len(matriz2)
    n = len(matriz2[0])
    for i in range(len(res)):
        for j in range(len(res[0])):
            res[i][j] = comp.multiplicar(matriz1[i//m][j//n],matriz2[i%m][j%n])
    return res

def verificarcuantico(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j][1] != 0 or matriz[i][j][0] < 0:
                return True
    return False

def modulomatriz(matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = [comp.modulo(matriz[i][j])**2,0]
    return matriz



    
def main():
##    """Pruebas"""
##    m1 = [[[8,3]],[[-1,-4]],[[0,-9]]]
##    m2 = [[[8,-3]],[[2,5]],[[3,0]]]
##    print(sumamatriz(m1,m2))
##    print()
##    m3 = [[[-5,2]],[[3,0]],[[0,-1]]]
##    print(inversoadimatriz(m3))
##    print()
    m4 = [[[-2,5]],[[-1,-1]],[[2,-9]]]
    print(multescalarmatriz([-1,1],m4))
    print()
    m5 = [[[-8,-3],[-6,-4],[0,-4]],[[-1,8],[6,-10],[8,-5]],[[4,0],[8,5],[-7,-9]]]
    m6 = [[[-7,-2],[-4,-2],[7,7]],[[5,9],[0,3],[6,-5]],[[1,5],[-6,-6],[5,8]]]
    print(sumamatriz(m5,m6))
    print()
    m7 = [[[7,3],[-1,7]],[[-9,-4],[-7,-9]]]
    print(inversoadimatriz(m7))
    print()
    m8 = [[[3,-2],[8,-4]],[[4,-10],[-2,-8]]]
    print(multescalarmatriz([-2,3],m8))
    print()
    m9 = [[[5,9],[-7,-5],[-1,-4]],[[8,2],[-3,-7],[7,-8]]]
    print(transpuesta(m9))
    print()
    m10 = [[[-6,1],[3,8]],[[2,-6],[3,0]]]
    print(conjugadamatriz(m10))
    print()












    
    m11 = [[[7,7],[3,8],[8,4]],[[5,0],[8,-6],[-10,-1]]]
    print(adjuntamatriz(m11))
    print()
    m12 = [[[-6,2],[0,6],[7,2]],[[6,9],[7,7],[-6,-6]],[[5,8],[-6,8],[6,9]]]
    m13 = [[[9,-6],[-3,-4],[5,-2]],[[3,6],[-1,-5],[0,-5]],[[9,9],[8,-4],[-8,-4]]]
    print(multiplicarmatriz(m12,m13))
    print()
    m131 = [[[2,1],[3,0],[1,-1]],[[0,0],[0,-2],[7,-3]],[[3,0],[0,0],[1,-2]]]
    m132 = [[[0,-1],[1,0]],[[0,0],[0,1]]]
    mostrar(multiplicarmatriz(m131,m132))
    
    print()
    m14 = [[[-1,5],[1,-7],[-6,3]],[[-3,-9],[2,-5],[1,-10]],[[-6,5],[6,-5],[3,-2]]]
    v1 = [[[1,-3]],[[4,3]],[[-3,1]]]
    print(multiplicarmatriz(m14,v1))
    print()
    v2 = [[[2,-1]],[[-8,-5]],[[-2,-6]]]
    v3 = [[[6,-3]],[[5,-1]],[[-6,-2]]]
    print(productinterno(v2,v3))
    print()
    v4 = [[[4,5]],[[3,1]],[[0,-7]]]
    print(int(normavector(v4)))
    print()
    v5 = [[[2,7]],[[4,-1]],[[2,-4]]]
    v6 = [[[7,8]],[[2,-8]],[[1,4]]]
    print(round(distanciavectores(v5,v6),2))
    v7 = [[[9,-7]],[[-1,-6]]]
    v8 = [[[7,-8]],[[5,-9]]]
    print(round(distanciavectores(v7,v8),2))
    print()
    m15 = [[[(1/(2**0.5)),0],[0,(1/(2**0.5))]],[[0,(1/(2**0.5))],[(1/(2**0.5)),0]]]
    print(matrizunitaria(m15))
    print()
    m16 = [[[0,1],[1,0],[0,0]],[[0,0],[0,1],[1,0]],[[1,0],[0,0],[0,1]]]
    print(matrizunitaria(m16))
    print()
    m17 = [[[3,0],[2,-1],[0,-3]],[[2,1],[0,0],[1,-1]],[[0,3],[1,1],[0,0]]]
    print(matrizhermitiana(m17))
    print()
    m18 = [[[1,0],[3,-1]],[[3,1],[0,1]]]
    print(matrizhermitiana(m18))
    print()
    m19 = [[[1,1],[0,0]],[[1,0],[0,1]]]
    m20 = [[[-1,2],[-2,-2],[0,2]],[[2,3],[3,1],[2,2]],[[-2,1],[1,-1],[2,1]]]
    print(productotensorial(m19,m20))
#main()
