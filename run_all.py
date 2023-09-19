# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/9/18 17:44
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : run_all.py
# @Software : PyCharm
import pytest
import os

pytest.main(["-s", "-v", "--alluredir=../outFiles/reports/tmp", "--clean-alluredir"])
