import pytest
from src.make_a_dict import make_a_dict

class TestMakeADict:

    def test_make_a_dict(self):
        my_dict = make_a_dict(2, 3)
        expected_dict = {"a": 2, "b": 3, "result": 5}

        assert my_dict == expected_dict

from src.make_a_dict import persona
class TestPersona:

    @pytest.fixture
    def persona():
        return Persona(nombre="foo", edad=30, profesion='contador')

    def test_years_until_retirement(self):
        assert year_until_retirement(persona) == 35


    def test_name_and_age(self):
        assert name_and_age(persona) == ('foo', 30)



if __name__ == '__main__':
    pytest.main()