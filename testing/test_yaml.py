"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# pip install pyyaml
import yaml


def test_yml():
    with open("./datas/demo.yml") as f:
        result = yaml.safe_load(f)
    print(result)
    print(result.get("add").get("datas"))
