import os
import yaml
from pythoncode.calculator import Calculator
import pytest

def get_dates():
    with open("./data/mul.yaml") as f:
        dates = yaml.safe_load(f)
        add_dates = dates["datas"][0]
        add_ids = dates["myid"]
        print(type(add_dates["add"]))
        print(type(add_ids))
        return [add_dates["add"], add_ids]

class TestCale():
    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    # @pytest.mark.parametrize("a,b,expect", [
    #     (3, 5, -2), (-1, -2, 1), (100, 300, -200),
    # ], ids=["int", "minus", "bigint"])
    # def test_sub(self, a, b, expect):
    #     assert expect == self.cal.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", get_dates(), ids=get_dates()[1])
    def test_add(self, a, b, expect):
        print(">>>", get_dates()[0])
        assert expect == self.cal.add(a, b)

    # @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("./data/mul.yaml"))["datas"][1],\
    #                          ids=yaml.safe_load(open("./data/mul.yaml"))["myid"])
    # def test_mul(self, a, b, expect):
    #     assert expect == self.cal.mul(a, b)

    # @pytest.mark.parametrize("a,b,expect", [
    #     (3, 5, 0.6), (1, 1, 1), (16, 2, 8),
    # ])
    # def test_div(self, a, b, expect):
    #     assert expect == self.cal.div(a, b)

if __name__ == '__main__':
    pytest.main(["test_calc.py", "-sv", "--alluredir", "./allure-results/"])
    os.system(r"allure generate allure-results -o allure-report --clean")
    os.system(r"allure open allure-report")