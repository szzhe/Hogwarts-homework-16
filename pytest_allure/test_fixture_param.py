import pytest

actual_url = ["www.baidu.com", "www.google.com"]
expect_url = ["www.baidu.com", "www.google.com"]


# 方法一：param
@pytest.fixture(params=actual_url)
def back_actual_url(request):
    return request.param

# 方法二：param+ids
# @pytest.fixture(params=actual_url, ids=['baidu', 'google'])
# def back_actual_url(request):
#     return request.param

# 方法三：param+ids，ids函数调用
# def idfunc(actual_url):
#     if actual_url == "www.baidu.com":
#         return "baidu"
#     else:
#         return None
#
# @pytest.fixture(params=actual_url, ids=idfunc)
# def back_actual_url(request):
#     return request.param

# def test_url(back_actual_url):
#     assert back_actual_url in actual_url

# 方法四：同一个测试方法同时调用两个fixture

# @pytest.fixture(params=actual_url)
# def back_actual_url(request):
#     return request.param
#
# @pytest.fixture(params=expect_url)
# def back_expect_url(request):
#     return request.param
#
# def test_url(back_actual_url, back_expect_url):
#     assert back_actual_url == back_expect_url

if __name__ == '__main__':
    pytest.main(["test_fixture_param.py"])
