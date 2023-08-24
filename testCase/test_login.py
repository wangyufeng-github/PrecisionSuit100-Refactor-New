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
        subprocess.run(["airtest", "run", air_path + r"\test_login.air"])
        time.sleep(2)
        # 登录成功后断言搜索框是否存在
        result = judge_image_exist("test_login")
        assert_exists(Template(r"E:\project\PrecisionSuit100-Pytest+Airtest+UIautomation+Allure\image\template\test_login.png"))
        assert_that(result).is_true()



if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py', '--alluredir', report_path, '--clean-alluredir'])
    os.system(f'allure serve {report_path}')
