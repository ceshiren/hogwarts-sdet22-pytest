"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import logging
import time

import pytest

# fixture 方法
# 相当于setup teardown  更灵活
from pythoncode.calculator import Calculator


@pytest.fixture()
def login():
    # setup
    print("登录")
    # 相当于return
    yield ["token", "aaa"]
    # teardown
    print("登出操作")


@pytest.fixture()
def get_calc():
    # print("开始计算")
    logging.info("开始计算")
    calc = Calculator()
    # yield关键字可以激活后面的teardown操作
    yield calc
    # print("结束计算")
    logging.info("结束计算")


# autouse= True 自动应用执行
# autouse默认为False，需要在测试用例中引用fixture的名字才能执行
@pytest.fixture(scope="session", autouse=True)
def finish():
    yield
    # print("====>>>结束测试....")
    logging.info("====>>>结束测试....")


@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y%m%d_%H%M%S")
    log_name = './log/' + now + '.log'

    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(log_name)


@pytest.fixture(params=[["文", 9.3, "TypeError"], [4, "字", "TypeError"]], ids=["第一个参数是中文", "第二个参数是中文"])
def get_error_data(request):
    # 一定使用request 参数，以及通过 request.param 来获取每一组测试数据
    return request.param


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
