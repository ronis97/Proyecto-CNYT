"""
Libreria de complejos, en la cual por medio de arreglos, realizamos las operaciones basicas sumar, restar, multiplicar y dividir.
Luego procedemos a conversiones cartesiana y polar. Se incluye tambien funciones que permitiran encontrar el modulo, el conjugado
y la fase de un numero complejo. Por ultimo, se incluye una funcion que muestra en pantalla la notacion a + bi de un numero complejo.
"""
import math
from sys import stdin

def suma(num1,num2):
    """Suma de dos numeros complejos, num1 y num2 deben ser arreglos"""
    c = num1[0] + num2[0]
    d = num1[1] + num2[1]
    tot = [c,d]
    return tot

def resta(num1,num2):
    """Resta de dos numeros complejos, num1 y num2 deben ser arreglos"""
##    if num1[0] == 0 and num2[0] == 0:
##        return "No se puede resolver"
    c = num1[0] - num2[0]
    d = num1[1] - num2[1]
    tot = [c,d]
    return tot

def multiplicar(num1,num2):
    """Multiplicacion de dos numeros complejos, num1 y num2 deben ser arreglos"""
##    if num1[0] == 0 and num2[0] == 0:
##        return "No se puede resolver"
    c = num1[0]*num2[0] - num1[1]*num2[1]
    d = num1[0]*num2[1] + num1[1]*num2[0]
    tot = [c,d]
    return tot

def dividir(num1,num2):
    """Division de dos numeros complejos, num1 y num2 deben ser arreglos"""
    nume1 = num1[0] * num2[0] + num1[1]* num2[1]
    deno = num2[1]**2 + num2[1]**2
    nume2 = num1[1]*num2[0] - num1[0]*num2[1]
    if deno == 0:
        print("Division por cero es invalida")
    c = nume1/deno
    d = nume2/deno
    tot = [c,d]
    return tot

def inversoaditivo(num):
    """Retorna el inverso aditivo de un numero complejo"""
    x = -1 * num[0]
    y = -1 * num[1]
    return [x,y]

def escalarpornum(esc,num):
    
    res = multiplicar(esc,num)
    return res

def conjugado(num):
    """conjugado de un numero complejo, num debe ser un arreglo"""
    d = num[1]
    d = -d
    return [num[0],d]

def modulo(num):
    """Modulo de un numero complejo, num debe ser un arreglo """
    x,y = separar(num)
    c = x**2 + y **2     
    return c**0.5

def fase_complejo(num):
    """Fase, argumento o amplitud de un numero complejo, num debe ser un arreglo"""
    x = num[0]
    y = num[1]
    return math.atan2(y,x)
def pasar_a_polar(num):
    """Convertir un numero complejo a forma polar """
    r = modulo(num)
    theta = fase_complejo(num)
    pol = [r,theta]
    return pol

def pasar_a_cartesiana(num):
    """Convertir un numero complejo de forma polar a cartesiana """
    r = num[0]
    theta = num[1]
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return [x,y]

def separar(num):
    """Retorna parte real e imaginaria"""
    x = num[0]
    y = num[1]
    return x,y

def mostrar(n):
    """a es la parte real y b es la parte imaginaria
    muestra el numero complejo en forma a + bi"""
    a = n[0]
    b = n[1]
    if b > 0:       
        print(a,'+',str(b)+'i')
    elif b == 0:
        print(a)
    elif b < 0:
        print(a,'-',str(abs(b))+'i')
        
def main():
    n1 = [2,3]
    n2 = [1,0]
    n3 = suma(n1,n2)
    n4 = multiplicar(n1,n2)
    n5 = dividir([-7,3],[1,1])
    n6 = conjugado(n1)
    n7 = [1,1]
    pr = fase_complejo(n7)
    n8 = pasar_a_polar(n7)
    #print(n5)
    #mostrar(n1)
    #mostrar(n2)
    #mostrar(n3)
    #mostrar(n4)
    #mostrar(n5)
    #mostrar(n6)
    #print(pr)
    #print(n8)
   
#main()
