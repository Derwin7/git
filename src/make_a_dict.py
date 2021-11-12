import pytest


@pytest.fixture
def persona():
    return Persona(nombre="foo", edad=30, profesion='contador')


def make_a_dict(a, b):
    operation = a + b

    return {"a": a, "b": b, "result": operation}