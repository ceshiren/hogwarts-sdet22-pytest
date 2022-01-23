"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import pytest

from pythoncode.calculator import Calculator

"""
pytest规范：
文件名：test_开头 或者 以_test结尾
类名:Test开头
方法名： test_开头
"""


class TestCalc:
    def setup_class(self):
        # 通过 self. 让calc 变成实例变量，在用例里就可以被调用到了
        self.calc = Calculator()

    def setup(self):
        # 每条测试用例之前调用
        print("开始计算")

    def teardown(self):
        # 每条用例执行之后 被调用
        print("结束计算")

    def teardown_class(self):
        # 类里面所有的用例执行完成 之后会被调用，一个类只调用一次
        print("结束测试")

    # 添加标签 add标签
    @pytest.mark.add
    @pytest.mark.P0
    def test_add1(self):
        # 测试相加方法
        # 实例化
        # calc = Calculator()
        result = self.calc.add(1, 1)
        print(result)
        # 断言  预期结果与实际结果对比
        assert 2 == result

    @pytest.mark.add
    @pytest.mark.P0
    def test_add2(self):
        # calc = Calculator()
        result = self.calc.add(-0.01, 0.02)
        assert 0.01 == result

    @pytest.mark.add
    @pytest.mark.P0
    def test_add3(self):
        # calc = Calculator()
        result = self.calc.add(10, 0.02)
        assert 10.02 == result

    @pytest.mark.add
    @pytest.mark.P1
    def test_add4(self):
        # calc = Calculator()
        result = self.calc.add(98.99, 99)
        assert 197.99 == result

    @pytest.mark.add
    @pytest.mark.P1
    def test_add5(self):
        # calc = Calculator()
        result = self.calc.add(99, 98.99)
        assert 197.99 == result

    @pytest.mark.add
    @pytest.mark.P1
    def test_add6(self):
        # calc = Calculator()
        result = self.calc.add(-98.99, -99)
        assert -197.99 == result

    @pytest.mark.add
    @pytest.mark.P1
    def test_add7(self):
        # calc = Calculator()
        result = self.calc.add(-99, -98.99)
        assert -197.99 == result
