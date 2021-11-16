import pytest
from src.persona import persona


class TestPersona:

    def test_years_until_retirement(self, persona):
        assert years_until_retirement(persona) == 35


    def test_name_and_age(self):
        assert name_and_age(persona) == ('foo', 30)


if __name__ == '__main__':
    pytest.main()