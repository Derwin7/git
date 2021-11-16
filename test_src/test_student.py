import pytest
from datetime import datetime
from src.student import Student



@pytest.fixture
def dummy_student():
    return Student('Nikhil', datetime(2000, 1, 1), 'coe')

def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now()-dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age


if __name__ == '__main__':
    pytest.main()

