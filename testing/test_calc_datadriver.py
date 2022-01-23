"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import pytest
import yaml

from pythoncode.calculator import Calculator

"""
pytest规范：
文件名：test_开头 或者 以_test结尾
类名:Test开头
方法名： test_开头
"""


# 读取 yaml 数据文件
def get_data(level):
    with open("./datas/datas.yml", encoding="utf-8") as f:
        result = yaml.safe_load(f)
        add_data = result.get("add")
    return add_data.get(level).get("datas"), add_data.get(level).get("ids")


def test_getdata():
    add_P0_data, add_P0_ids = get_data("P0")
    add_P1_1_data, add_P1_1_ids = get_data("P1_1")
    add_P1_2_data, add_P1_2_ids = get_data("P1_2")
    add_P2_data, add_P2_ids = get_data("P2")
    print(add_P0_data, add_P0_ids)
    print(add_P1_1_data, add_P1_1_ids)
    print(add_P1_2_data, add_P1_2_ids)
    print(add_P2_data, add_P2_ids)


class TestCalc:
    add_P0_data, add_P0_ids = get_data("P0")
    add_P1_1_data, add_P1_1_ids = get_data("P1_1")
    add_P1_2_data, add_P1_2_ids = get_data("P1_2")
    add_P2_data, add_P2_ids = get_data("P2")

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
    @pytest.mark.parametrize("a,b,expect", add_P0_data, ids=add_P0_ids)
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
    @pytest.mark.parametrize("a,b,expect", add_P1_1_data, ids=add_P1_1_ids)
    def test_add2(self, a, b, expect):
        """
        【边界】P1:有效、无效边界值相加，结果计算正确
        :return:
        """
        result = self.calc.add(a, b)
        assert expect == result

    @pytest.mark.P12
    @pytest.mark.parametrize("a,b,expect", add_P1_2_data, ids=add_P1_2_ids)
    def test_add_errorP12(self, a, b, expect):
        # eval("")将字符串转成对象
        with pytest.raises(eval(expect)) as e:
            result = self.calc.add(a, b)
        # 断言
        # e.typename 获取断言的类型
        assert expect == e.typename

    @pytest.mark.P2
    @pytest.mark.parametrize("a,b,expect", add_P2_data, ids=add_P2_ids)
    def test_add_error_P2(self, a, b, expect):
        # eval("")将字符串转成对象
        with pytest.raises(eval(expect)) as e:
            result = self.calc.add(a, b)
        # 断言
        # e.typename 获取断言的类型
        # assert expect == e.typename
