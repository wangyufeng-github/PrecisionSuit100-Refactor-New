# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/8/23 10:56
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : conftest.py
# @Software : PyCharm

import pytest,time,subprocess,os
from configs.config import log_path,app_path,app_process_name
from utils.common import clear_folder,kill_process_by_name,start_application


@pytest.fixture(scope="session", autouse=True)
def start_app():
    # 清空日志文件
    clear_folder(log_path)
    subprocess.Popen(app_path, cwd=os.path.dirname(app_path))
    time.sleep(3)
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
