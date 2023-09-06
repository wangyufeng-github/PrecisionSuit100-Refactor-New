# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/8/22 14:38
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : test_login.air.py
# @Software : PyCharm
import pytest, subprocess
from airtest.core.api import *
from airtest.core.api import Template
from configs.config import *
from utils.common import *
from assertpy import *


class TestLogin:
    def test_login(self):
        try:
            result = subprocess.run(
                ["airtest", "run", air_path + r"\test_login.air"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,  # 文本模式，以便捕获文本输出
                check=True  # 检查返回代码以捕获异常
            )

            # 处理标准输出和标准错误输出
            # stdout_output = result.stdout
            # stderr_output = result.stderr

            # print("标准输出:")
            # print(stdout_output)
            #
            # print("标准错误输出:")
            # print(stderr_output)

        except subprocess.CalledProcessError as e:
            # 处理命令行命令引发的异常
            # print(f"命令行命令执行异常，返回代码: {e.returncode}")
            # print(f"标准输出: {e.stdout}")
            # print(f"标准错误输出: {e.stderr}")
            pytest.fail("用例执行失败,请通过日志定位问题")


if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py', '--alluredir', report_path, '--clean-alluredir'])
    os.system(f'allure serve {report_path}')
