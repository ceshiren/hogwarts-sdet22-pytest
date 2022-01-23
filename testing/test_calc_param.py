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
    @pytest.mark.parametrize("a,b,expect", [[1, 1, 2], [-0.01, 0.02, 0.01], [10, 0.02, 10.02]])
    def test_add1(self, a, b, expect):
        """
        【正向】P0 :2个整数相加，结果计算正确
        :return:
        """
        result = self.calc.add(a, b)
        assert expect == result

    # 添加标签 add标签
    @pytest.mark.add
    @pytest.mark.P1
    @pytest.mark.parametrize("a,b,expect", [
        [98.99, 99, 197.99], [99, 98.99, 197.99],
        [-98.99, -99, -197.99], [-99, -98.99, -197.99]

    ])
    def test_add2(self, a, b, expect):
        """
        【边界】P1:有效边界值相加，结果计算正确
        :return:
        """
        result = self.calc.add(a, b)
        assert expect == result

    @pytest.mark.add
    @pytest.mark.P1
    @pytest.mark.parametrize("a,b,expect", [
        [99.01, 0, "参数大小超出范围"],
        [-99.01, -1, "参数大小超出范围"],
        [2, 99.01, "参数大小超出范围"],
        [1, -99.01, "参数大小超出范围"]
    ])
    def test_add3(self, a, b, expect):
        """
        【边界】P1:无效边界值相加，给出提示信息
        :return:
        """
        result = self.calc.add(a, b)
        # 断言
        assert expect == result

    @pytest.mark.parametrize("a,b,expect", [["文", 9.3, "TypeError"], [4, "字", "TypeError"]],
                             ids=["第一个参数是中文", "第二个参数是中文"])
    def test_add_error(self, a, b, expect):
        # eval("")将字符串转成对象
        with pytest.raises(eval(expect)) as e:
            result = self.calc.add(a, b)
        # 断言
        # e.typename 获取断言的类型
        assert expect == e.typename
