from src import calculadora as calc
#import pytest

# calc es un alias que le damos a calculadora en el momento de la importación
# así evitamos tener que escribir el nombre completo.


def test_suma():
    suma = calc.suma(3, 2)
    assert suma == 5

def test_resta():
    resta = calc.resta(5, 2)
    assert resta == 3

def test_multiplicacion():
    multipli = calc.multiplicacion(4, 5)
    assert multipli == 20

def test_division():
    divi = calc.division(20, 2)
    assert divi == 10

def test_cuadrado():
    cuadrado = calc.cuadrado(4)
    assert cuadrado == 16

def test_factorial():
    fact = calc.factorial(5)
    assert fact == 120

def test_potenciacion():
    pote = calc.potenciacion(3, 3)
    assert pote == 27
