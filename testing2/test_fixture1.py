"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import pytest


# 执行这条用例之前 执行fixture
@pytest.mark.parametrize("a", [1, 2, 10])
def test_case1(a, login):
    print(f"fixture 返回值 ：{login}")
    print(f"参数：{a}")
    # 单张图片的展示情况
    # 先测试数据 ---- 1张图片
    print("test case1 --- 图片展示一张")


# 执行步骤一：
def test_data():
    print("准备测试数据")


# 执行步骤二：
def test_case10(login):
    # 单张图片的展示情况
    # 先测试数据 ---- 10张图片
    print("test case10 --- 图片展示10张")
    # 清除测试数据 --- 不影响 后续用例的执行


# 步骤三：清除数据
def test_clear():
    print("清降测试数据")


def test_case100(login):
    # 单张图片的展示情况
    # 先测试数据 ---- 100张图片
    print("test case100 --- 图片展示10张")


def test_case2():
    print("test case2 ----- 商品页功能")


def test_case3():
    print("test case3 ------ 搜索功能")
