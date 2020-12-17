import os
import yaml
import pytest

def get_dates():
    with open("../data/datas.yml") as f:
        dates = yaml.safe_load(f)
        # print(dates)
        add_dates = dates["add"]
        add_ids = dates["myid"]
        # print(">", add_dates)
        # print(">>", add_ids)
        return [add_dates, add_ids]

class TestCale():

    # @pytest_allure.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expect", get_dates()[0], ids=get_dates()[1])
    def test_add(self, a, b, expect, test_calc):
        # print(">>>", get_dates()[0])
        cal = test_calc
        assert expect == cal.add(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, -2), (-1, -2, 1), (100, 300, -200),
    ], ids=["int", "minus", "bigint"])
    def test_sub(self, a, b, expect, test_calc):
        cal = test_calc
        assert expect == cal.sub(a, b)

    # @pytest_allure.mark.run(order=1)
    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("../data/datas.yml"))["mul"],
                             ids=yaml.safe_load(open("../data/datas.yml"))["myid"])
    def test_mul(self, a, b, expect, test_calc):
        cal = test_calc
        assert expect == cal.mul(a, b)

    # @pytest_allure.mark.run(order=3)
    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, 0.6), (1, 1, 1), (16, 2, 8),
    ])
    def test_div(self, a, b, expect, test_calc):
        cal = test_calc
        assert expect == cal.div(a, b)

if __name__ == '__main__':
    pytest.main(["test_calc.py", "-sv", "--alluredir", "../allure-results/"])
    os.system(r"allure generate ../allure-results -o ../allure-report --clean")
    os.system(r"allure open ../allure-report")
