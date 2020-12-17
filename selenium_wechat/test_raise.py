# coding=utf-8

import pytest


def division(a, b):
    return int(a / b)


@pytest.mark.parametrize('a, b, c', [(4, 2, 2), (0, 2, 0), (1, 0, pytest.raises(ZeroDivisionError)), (6, 8, 0)],
                         ids=['整除', '被除数为0', '除数为0', '非整除'])
def test_2(a, b, c):
    if b == 0:
        with c:
            assert division(a, b) is not None
    else:
        assert division(a, b) == c


if __name__ == '__main__':
    pytest.main(["test_raise.py", "-s", "-v"])
