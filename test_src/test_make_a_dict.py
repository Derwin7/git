import pytest
from src.make_a_dict import make_a_dict


class TestMakeADict:

    def test_make_a_dict(self):
        my_dict = make_a_dict(2, 3)
        expected_dict = {"a": 2, "b": 3, "result": 5}

        assert my_dict == expected_dict


if __name__ == '__main__':
    pytest.main()