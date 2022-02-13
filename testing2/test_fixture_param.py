"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import pytest


@pytest.fixture(params=[[1, 1, 3], [0.1, 0.1, 0.2]], ids=["int", "float"])
def get_datas(request):
    # 通过 request.param 拿到每一组测试数据
    return request.param


def test_p(get_datas):
    a = get_datas[0]
    b = get_datas[1]
    expect = get_datas[2]
    assert a + b == expect


@pytest.fixture(params=[[1, 1, 2], [0.1, 0.1, 0.2]], ids=["int", "float"])
def get_param(request):
    return request.param


def test_param(get_param):
    print(f"{get_param[0], get_param[1], get_param[2]}")
