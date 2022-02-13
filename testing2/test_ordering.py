"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import logging

# pytest 用例执行顺序
# unittest  测试用例的名字 排序，ASCII 码
import pytest


@pytest.mark.run(order=2)
def test_case1():
    logging.info("用例1 ")


@pytest.mark.run(order=1)
def test_case2():
    logging.info("用例2 ")


def test_case4():
    logging.info("用例4 ")


def test_case0():
    logging.info("用例0 ")


def test_casea():
    logging.info("用例a ")


@pytest.mark.run(order=-5)
def test_case3():
    logging.info("用例3 ")
