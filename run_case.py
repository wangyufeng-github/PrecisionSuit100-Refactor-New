# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/9/13 11:34
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : run_case.py
# @Software : PyCharm
import os
import pytest
from configs.config import test_case_path

if __name__ == "__main__":
    # 切换到包含测试文件的目录
    os.chdir(test_case_path)
    # 运行pytest测试
    pytest.main()
