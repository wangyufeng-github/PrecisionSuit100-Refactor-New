# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/8/23 10:56
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : conftest.py
# @Software : PyCharm

import pytest

from utils.common import *


@pytest.fixture(scope="session", autouse=True)
def start_app():
    subprocess.Popen(r"C:\wemed\PrecisionSuit100\PrecisionSuit100Application.exe", cwd=r"C:\wemed\PrecisionSuit100")
    time.sleep(5)
    # window_handle = get_window_handle("LoginWindow")
    # connect_to_window(window_handle=window_handle)
    yield
    kill_process_by_name(process_name=app_process_name)


if __name__ == '__main__':
    start_application(app_path)
    time.sleep(5)
    # window_handle = get_window_handle("LoginWindow")
    # connect_to_window(window_handle=window_handle)
    # time.sleep(2)
    subprocess.run(["airtest", "run",
                    r"E:\project\PrecisionSuit100-Pytest+Airtest+UIautomation+Allure\air\test_login.air"])
