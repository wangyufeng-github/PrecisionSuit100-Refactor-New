# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2023/8/22 11:35
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : config.py
# @Software : PyCharm
import os

# 工程路径
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# air文件路径
air_path = os.path.join(root_path, 'air')
# 日志文件路径
log_path = os.path.join(root_path, 'outFiles\\logs')
# 报告文件路径
report_path = os.path.join(root_path, 'outFiles\\reports')
# 截图路径
screen_shot_path = os.path.join(root_path, 'outFiles\\screenshot')
# 图片路径
image_path = os.path.join(root_path, 'image')
# 进程名称
app_process_name = "PrecisionSuit100Application.exe"
# 可执行程序路径
app_path = r"C:\wemed\PrecisionSuit100\PrecisionSuit100Application.exe"
# 配置文件路径
user_info_path = os.path.join(root_path, 'data\\user_info.ini')
# 测试用例执行路径
test_case_path = os.path.join(root_path, 'testCase')
# 虚拟环境python.exe路径
virtualenv_python = r"E:\env\venv_Precisionsuit100-RF-test\Scripts\python.exe"

if __name__ == '__main__':
    print(test_case_path)
