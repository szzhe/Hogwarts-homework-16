import pytest
from pom_xueqiu.base_page import BasePage


class TestDD:
    def test_dd(self):
        base = BasePage()
        base.steps("../testcase/steps.yaml")

    def test_search(self):
        pass


if __name__ == '__main__':
    pytest.main(["test_dd.py", "-v", "-s"])
