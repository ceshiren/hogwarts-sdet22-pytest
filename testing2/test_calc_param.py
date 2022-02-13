"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import allure
import pytest

from pythoncode.calculator import Calculator

"""
pytest规范：
文件名：test_开头 或者 以_test结尾
类名:Test开头
方法名： test_开头
"""


# 大类别 feature
# 小类别 story

@allure.feature("计算器功能")
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
    @pytest.mark.parametrize("a,b,expect", [[1, 1, 3], [-0.01, 0.02, 0.01], [10, 0.02, 10.02]])
    @pytest.mark.run(order=3)
    @allure.story("相加功能P0")
    def test_add1(self, login, a, b, expect):
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
    @pytest.mark.run(order=1)
    @allure.story("相加功能P1")
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
    @pytest.mark.run(order=2)
    @allure.story("相加功能-超出范围")
    def test_add3(self, a, b, expect):
        """
        【边界】P1:无效边界值相加，给出提示信息
        :return:
        """
        with allure.step("步骤一：执行相加操作"):
            result = self.calc.add(a, b)
        # 断言
        with allure.step("步骤二：断言"):
            allure.attach.file("/Users/juanxu/Downloads/logo.jpg",
                               name="图片",
                               attachment_type=allure.attachment_type.JPG,
                               extension=".jpg")
            assert expect == 2

    @pytest.mark.run(order=-1)
    @allure.story("相加功能-error")
    def test_add_error(self, get_error_data):
        a = get_error_data[0]
        b = get_error_data[1]
        expect = get_error_data[2]
        # eval("")将字符串转成对象
        with pytest.raises(eval(expect)) as e:
            result = self.calc.add(a, b)
        # 断言
        # e.typename 获取断言的类型
        assert expect == e.typename
