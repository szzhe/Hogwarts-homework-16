import pytest
from pythoncode.calculator import Calculator


@pytest.fixture(scope="class")
def test_calc():
    print("开始计算")
    cal = Calculator()
    yield cal
    print("结束计算")
