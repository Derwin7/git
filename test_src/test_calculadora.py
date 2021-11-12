from src import calculadora as calc
import pytest


# calc es un alias que le damos a calculadora en el momento de la importación
# así evitamos tener que escribir el nombre completo.

class TestCalculadora:

    def test_suma(self):
        self.suma = calc.suma(3, 2)
        assert self.suma == 5

    def test_resta(self):
        self.resta = calc.resta(5, 2)
        assert self.resta == 3

    def test_multiplicacion(self):
        self.multipli = calc.multiplicacion(4, 5)
        assert self.multipli == 20

    def test_division(self):
        self.divi = calc.division(20, 2)
        assert self.divi == 10

    def test_cuadrado(self):
        self.cuadrado = calc.cuadrado(4)
        assert self.cuadrado == 16

    def test_factorial(self):
        self.fact = calc.factorial_1(5)
        assert self.fact == 120

    def test_potenciacion(self):
        self.pote = calc.potenciacion(3, 3)
        assert self.pote == 27


if __name__ == '__main__':
    pytest.main()
