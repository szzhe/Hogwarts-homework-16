
import pytest

def add_function(a, b):
    return a + b

@pytest.mark.parametrize("a,b,expected", [
    (3, 5, 8), (-1, -2, -3), (1000, 1000, 2000)
], ids=["int", "minus", "bigint"])
def test_add(a, b, expected):
    assert add_function(a, b) == expected

@pytest.mark.demo
@pytest.mark.parametrize("a", [0, 1, 5])
@pytest.mark.parametrize("b", [2, 3, 8])
def test_add1(a, b):
    print("测试数据组合：\
    a->%s, b->%s" % (a, b))

class Test_Demo():
    @pytest.mark.demo
    def test_demo(self):
        a = 5
        b = -1
        assert a != b
        print("我的第一个测试用例")

    @pytest.mark.demo
    @pytest.mark.smoke
    def test_two(self):
        a = 2
        b = -1
        assert a != b
        print("我的第二个测试用例")

if __name__ == '__main__':
    pytest.main(['test_mark.py'])