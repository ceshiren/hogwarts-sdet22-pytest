"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from pythoncode.calculator import Calculator

"""
pytest规范：
文件名：test_开头 或者 以_test结尾
类名:Test开头
方法名： test_开头
"""


class TestCalc:
    def test_add(self):
        # 测试相加方法
        # 实例化
        calc = Calculator()
        result = calc.add(1, 1)
        print(result)
        # 断言  预期结果与实际结果对比
        assert 2 == result
