import pytest


def add_function(a, b):
    return a + b


@pytest.mark.parametrize("a,b,expected", [
    (3, 5, 8), (-1, -2, -3), (1000, 1000, 2000)
], ids=["int", "minus", "bigint"])
def test_add(a, b, expected):
    assert add_function(a, b) == expected


@pytest.mark.parametrize("a", [0, 1, 5])
@pytest.mark.parametrize("b", [2, 3, 8])
def test_add1(a, b):
    print("测试数据组合：\
    a->%s, b->%s" % (a, b))


if __name__ == '__main__':
    pytest.main(['-sq', 'test_dome.py'])
