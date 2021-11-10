from math import factorial


def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1-num2

def multiplicacion(num1, num2):
    return num1*num2

def division(num1, num2):
    return num1/num2

def cuadrado(num1):
    return num1**2

def factorial(num1):
    for i in range(1, num1):
        num1 = num1*i
    return num1

def potenciacion(num1, num2):
    return num1**num2
