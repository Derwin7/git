from src import calculadora as calc
import pytest


# calc es un alias que le damos a calculadora en el momento de la importación
# así evitamos tener que escribir el nombre completo.

class TestCalculadora:

    def test_suma(self):
        suma = calc.suma(3, 2)
        assert suma == 5

    def test_resta(self):
        resta = calc.resta(5, 2)
        assert resta == 3

    def test_multiplicacion(self):
        multipli = calc.multiplicacion(4, 5)
        assert multipli == 20

    def test_division(self):
        divi = calc.division(20, 2)
        assert divi == 10

    def test_cuadrado(self):
        cuadrado = calc.cuadrado(4)
        assert cuadrado == 16

    def test_factorial(self):
        fact = calc.factorial_1(5)
        assert fact == 120

    def test_potenciacion(self):
        pote = calc.potenciacion(3, 3)
        assert pote == 27


if __name__ == '__main__':
    pytest.main()
