"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import logging

import pytest


class TestCalaculator:
    # 添加标签 add标签
    @pytest.mark.add
    @pytest.mark.P0
    @pytest.mark.parametrize("a,b,expect", [[1, 1, 2], [-0.01, 0.02, 0.01], [10, 0.02, 10.02]])
    def test_add1(self, get_calc, a, b, expect):
        """
        【正向】P0 :2个整数相加，结果计算正确
        :return:
        """
        logging.info("加法用例P0级别")
        logging.info(f"输入数据：{a, b},预期数据：{expect}")
        result = get_calc.add(a, b)
        assert expect == result
